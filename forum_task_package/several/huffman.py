# import os
# import marshal
# import _pickle as cPickle
#
#
# class mynode(object):
#     rp = False
#
#     def __init__(self, ch=None, fq=None, lnode=None, rnode=None, parent=None):
#         self.L = lnode
#         self.R = rnode
#         self.p = parent
#         self.c = ch
#         self.fq = fq
#
#     def __repr__(self):
#         if mynode.rp:
#             lnonde = self.L if self.L else '#'
#             rnode = self.R if self.R else '#'
#             return ''.join(('(%s:%d)' % (self.c, self.fq), str(lnonde)))
#         else:
#             return '(%s:%d)' % (self.c, self.fq)
#
#     def __cmp__(self, other):
#         if not isinstance(othet, mynode):
#             return super(mynode, self).__cmp__(other)
#         return cmp(self.fq, other.fq)
#
#
# def pftn(nodes):
#     if len(nodes) > 1:
#         first = nodes.pop(0)
#         second = nodes.pop(0)
#         return first, second
#     else:
#         return nodes[0], None
#
#
# if __name__ == '__main__':
#     orig_fl = 'filename.txt'
#     comp_file = 'compr.swc'
#     dec_file = 'filename.txt'
#     enc = encoder(orig_file)
#     enc.wrie(comp_file)
#     dec = decoder(comp_file)
#     dec.decode_as(dec_file)
