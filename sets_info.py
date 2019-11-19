def sets_info(table_a, table_b, col_a, col_b):
    '''
    print set informations about values in 2 columns
    usefull for various ids
    '''

    a = frozenset(spark.table(table_a).rdd.map(lambda x: getattr(x, col_a)).distinct().collect())
    b = frozenset(spark.table(table_b).rdd.map(lambda x: getattr(x, col_b)).distinct().collect())
    
    print('a = {}.{}'.format(table_a, col_a))
    print('b = {}.{}'.format(table_b, col_b))
    print('a | b:', len(a | b))
    print('a & b:', len(a & b))
    print('a ^ b:', len(a ^ b))
    print('a - b:', len(a - b))
    print('b - a:', len(b - a))
    
