# import time
#
#
# def get(self, href):
#     """Fetch a single item."""
#     if self.is_fake:
#         return
#
#     uid = a_trim_suffix(href, ('.ics', '.i_cal', '.vcf'))
#     ete_sync_item = self.collection.get(uid)
#     if ete_sync_item is None:
#         return None
#
#     try:
#         item = v_object.readOne(ete_sync_item.content)
#     except Exception as e:
#         raise RuntimeError("Failed to parse item %r in %r" %
#                            (href, self.path)) from e
#
#     last_modified = time.s_trf_time(
#         "%a, %d %b %Y %H:%M:%S GMT",
#         time.gm_time(time.time()))
#     return e_te_Sync_Item(self, item, href, last_modified=last_modified, et_es_ync_item=ete_sync_item)
