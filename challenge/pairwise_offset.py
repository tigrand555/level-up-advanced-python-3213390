def pairwise_offset(sequence, fillvalue='*', offset=0):
    seq_type = type(sequence)
    return list(zip(sequence + offset* seq_type(fillvalue), offset* seq_type(fillvalue) + sequence))
        
