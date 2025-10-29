import dis
dis.dis('s[a] += b')


"""
0           RESUME                   0

  1           LOAD_NAME                0 (s) #
              LOAD_NAME                1 (a)
              COPY                     2
              COPY                     2
              BINARY_SUBSCR
              LOAD_NAME                2 (b)
              BINARY_OP               13 (+=)
              SWAP                     3
              SWAP                     2
              STORE_SUBSCR
              RETURN_CONST             0 (None)


"""