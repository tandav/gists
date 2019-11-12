def last_partitions(table, n=3):
    _ = ['hive', '-e', 'show partitions {}'.format(table)]
    _ = subprocess.check_output(_)
    _ = _.decode()
    _ = _.splitlines()
    _ = _[1 : n + 1] # skip header
    _ = [x.split('=')[1] for x in _]
    return _
