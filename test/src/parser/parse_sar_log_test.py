import pytest
from unittest.mock import mock_open, patch
from src.parser.parse_sar_log import parse_sar_log

test_log_file = """
Linux 6.11.0-9-generic (ubuntu-s-1vcpu-2gb-ams3-01) 	11/10/24 	_x86_64_	(1 CPU)

19:10:04        CPU     %user     %nice   %system   %iowait    %steal     %idle
19:10:05        all      1.94      0.00      1.94      3.88      5.83     86.41
19:10:06        all      0.98      0.00      0.98      0.00      2.94     95.10
19:10:07        all      0.00      0.00      0.00      0.00      3.96     96.04
19:10:08        all      3.96      0.00      2.97      0.99      2.97     89.11
19:10:09        all      6.60      0.00      4.72      0.00      7.55     81.13
19:10:10        all      6.12      0.00      3.06      0.00      3.06     87.76
"""

@pytest.mark.parametrize("options, expected", [
    ({"ignore_end_lines": 0}, {"sample_count": 6}),
    ({"ignore_end_lines": 1}, {"sample_count": 5}),
    ({"ignore_end_lines": 2}, {"sample_count": 4}),
    ({"ignore_end_lines": 3}, {"sample_count": 3}),
    ({"ignore_end_lines": 4}, {"sample_count": 2}),
    ({"ignore_end_lines": 5}, {"sample_count": 1}),
])
def test_parse_sar_log_with_valid_partitions(options, expected):
    with patch("builtins.open", mock_open(read_data=test_log_file)):
        df = parse_sar_log("dummy_path.log", options["ignore_end_lines"])
        
        assert df["%User"].count() == expected["sample_count"]
        assert df["%Nice"].count() == expected["sample_count"]
        assert df["%System"].count() == expected["sample_count"]
        assert df["%IOWait"].count() == expected["sample_count"]
        assert df["%Steal"].count() == expected["sample_count"]
        assert df["%Idle"].count() == expected["sample_count"] 

@pytest.mark.parametrize("options, expected", [
    ({"log_file_path": "", "ignore_end_lines": 0}, {"error_type": ValueError, "error_message": "No log file specified"}),
    ({"log_file_path": 1, "ignore_end_lines": 0}, {"error_type": ValueError, "error_message": "Invalid log file; Must be a string"}),
    ({"log_file_path": "dummy_path.log", "ignore_end_lines": True}, {"error_type": ValueError, "error_message": "Invalid ignore_end_lines; Must be an integer"}),
    ({"log_file_path": "dummy_path.log", "ignore_end_lines": {"g":2}}, {"error_type": ValueError, "error_message": "Invalid ignore_end_lines; Must be an integer"}),
    ({"log_file_path": "dummy_path.log", "ignore_end_lines": -1}, {"error_type": ValueError, "error_message": "Invalid ignore_end_lines; Must be greater than or equal to 0"}),
    ({"log_file_path": "dummy_path.log", "ignore_end_lines": 1.0}, {"error_type": ValueError, "error_message": "Invalid ignore_end_lines; Must be an integer"}),
])
def test_parse_sar_log_with_invalid_partitions(options, expected):
    with patch("builtins.open", mock_open(read_data=test_log_file)):
        with pytest.raises(expected["error_type"], match=expected["error_message"]):
            parse_sar_log(options["log_file_path"], options["ignore_end_lines"])

def test_parse_sar_log_without_user():
    test_log_file_without_user = """
        Linux 6.11.0-9-generic (ubuntu-s-1vcpu-2gb-ams3-01) 	11/10/24 	_x86_64_	(1 CPU)

        19:10:04        CPU     %nice   %system   %iowait    %steal     %idle
        19:10:05        all      0.00      1.94      3.88      5.83     86.41
        19:10:06        all      0.00      0.98      0.00      2.94     95.10
        19:10:07        all      0.00      0.00      0.00      3.96     96.04
        19:10:08        all      0.00      2.97      0.99      2.97     89.11
        19:10:09        all      0.00      4.72      0.00      7.55     81.13
        19:10:10        all      0.00      3.06      0.00      3.06     87.76
    """
    with patch("builtins.open", mock_open(read_data=test_log_file_without_user)):
        with pytest.raises(ValueError, match="The parser could not find any valid lines: dummy_path.log; Ensure the file contains time, cpu, user, nice, system, iowait, steal, and idle fields. Also ensure it is not empty."):
            parse_sar_log("dummy_path.log", 0)

def test_parse_sar_log_without_nice():
    test_log_file_without_nice = """
        Linux 6.11.0-9-generic (ubuntu-s-1vcpu-2gb-ams3-01) 	11/10/24 	_x86_64_	(1 CPU)

        19:10:04        CPU     %user   %system   %iowait    %steal     %idle
        19:10:05        all      1.94      1.94      3.88      5.83     86.41
        19:10:06        all      0.98      0.98      0.00      2.94     95.10
        19:10:07        all      0.00      0.00      0.00      3.96     96.04
        19:10:08        all      3.96      2.97      0.99      2.97     89.11
        19:10:09        all      6.60      4.72      0.00      7.55     81.13
        19:10:10        all      6.12      3.06      0.00      3.06     87.76
    """
    with patch("builtins.open", mock_open(read_data=test_log_file_without_nice)):
        with pytest.raises(ValueError, match="The parser could not find any valid lines: dummy_path.log; Ensure the file contains time, cpu, user, nice, system, iowait, steal, and idle fields. Also ensure it is not empty."):
            parse_sar_log("dummy_path.log", 0)
            
def test_parse_sar_log_without_system():
    test_log_file_without_system = """
        Linux 6.11.0-9-generic (ubuntu-s-1vcpu-2gb-ams3-01) 	11/10/24 	_x86_64_	(1 CPU)

        19:10:04        CPU     %user     %nice   %iowait    %steal     %idle
        19:10:05        all      1.94      0.00      3.88      5.83     86.41
        19:10:06        all      0.98      0.00      0.00      2.94     95.10
        19:10:07        all      0.00      0.00      0.00      3.96     96.04
        19:10:08        all      3.96      0.00      0.99      2.97     89.11
        19:10:09        all      6.60      0.00      0.00      7.55     81.13
        19:10:10        all      6.12      0.00      0.00      3.06     87.76
    """
    with patch("builtins.open", mock_open(read_data=test_log_file_without_system)):
        with pytest.raises(ValueError, match="The parser could not find any valid lines: dummy_path.log; Ensure the file contains time, cpu, user, nice, system, iowait, steal, and idle fields. Also ensure it is not empty."):
            parse_sar_log("dummy_path.log", 0)
            
def test_parse_sar_log_without_iowait():
    test_log_file_without_iowait = """
        Linux 6.11.0-9-generic (ubuntu-s-1vcpu-2gb-ams3-01) 	11/10/24 	_x86_64_	(1 CPU)

        19:10:04        CPU     %user     %nice   %system    %steal     %idle
        19:10:05        all      1.94      0.00      1.94      5.83     86.41
        19:10:06        all      0.98      0.00      0.98      2.94     95.10
        19:10:07        all      0.00      0.00      0.00      3.96     96.04
        19:10:08        all      3.96      0.00      2.97      2.97     89.11
        19:10:09        all      6.60      0.00      4.72      7.55     81.13
        19:10:10        all      6.12      0.00      3.06      3.06     87.76
    """
    with patch("builtins.open", mock_open(read_data=test_log_file_without_iowait)):
        with pytest.raises(ValueError, match="The parser could not find any valid lines: dummy_path.log; Ensure the file contains time, cpu, user, nice, system, iowait, steal, and idle fields. Also ensure it is not empty."):
            parse_sar_log("dummy_path.log", 0)

def test_parse_sar_log_without_steal():
    test_log_file_without_steal = """
        Linux 6.11.0-9-generic (ubuntu-s-1vcpu-2gb-ams3-01) 	11/10/24 	_x86_64_	(1 CPU)

        19:10:04        CPU     %user     %nice   %system   %iowait     %idle
        19:10:05        all      1.94      0.00      1.94      5.83     86.41
        19:10:06        all      0.98      0.00      0.98      2.94     95.10
        19:10:07        all      0.00      0.00      0.00      3.96     96.04
        19:10:08        all      3.96      0.00      2.97      2.97     89.11
        19:10:09        all      6.60      0.00      4.72      7.55     81.13
        19:10:10        all      6.12      0.00      3.06      3.06     87.76
    """
    with patch("builtins.open", mock_open(read_data=test_log_file_without_steal)):
        with pytest.raises(ValueError, match="The parser could not find any valid lines: dummy_path.log; Ensure the file contains time, cpu, user, nice, system, iowait, steal, and idle fields. Also ensure it is not empty."):
            parse_sar_log("dummy_path.log", 0)
            
def test_parse_sar_log_without_idle():
    test_log_file_without_idle = """
        Linux 6.11.0-9-generic (ubuntu-s-1vcpu-2gb-ams3-01) 	11/10/24 	_x86_64_	(1 CPU)

        19:10:04        CPU     %user     %nice   %system   %iowait    %steal
        19:10:05        all      1.94      0.00      1.94      5.83     86.41
        19:10:06        all      0.98      0.00      0.98      2.94     95.10
        19:10:07        all      0.00      0.00      0.00      3.96     96.04
        19:10:08        all      3.96      0.00      2.97      2.97     89.11
        19:10:09        all      6.60      0.00      4.72      7.55     81.13
        19:10:10        all      6.12      0.00      3.06      3.06     87.76
    """
    with patch("builtins.open", mock_open(read_data=test_log_file_without_idle)):
        with pytest.raises(ValueError, match="The parser could not find any valid lines: dummy_path.log; Ensure the file contains time, cpu, user, nice, system, iowait, steal, and idle fields. Also ensure it is not empty."):
            parse_sar_log("dummy_path.log", 0)

def test_parse_sar_log_without_empty_log_file():
    with patch("builtins.open", mock_open(read_data="")):
        with pytest.raises(ValueError, match="The parser could not find any valid lines: dummy_path.log; Ensure the file contains time, cpu, user, nice, system, iowait, steal, and idle fields. Also ensure it is not empty."):
            parse_sar_log("dummy_path.log", 0)

def test_parse_sar_log_with_invalid_path():
    with patch("builtins.open", side_effect=FileNotFoundError):
        with pytest.raises(FileNotFoundError, match="No such file or directory: 'dummy_path.log'"):
            parse_sar_log("dummy_path.log", 0)
