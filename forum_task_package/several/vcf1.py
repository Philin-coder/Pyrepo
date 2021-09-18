def get(self, href):
    """Fetch a single item."""
    if self.is_fake:
        return

    uid = _trim_suffix(href, ('.ics', '.ical', '.vcf'))
    etesync_item = self.collection.get(uid)
    if etesync_item is None:
        return None

    try:
        item = vobject.readOne(etesync_item.content)
    except Exception as e:
        raise RuntimeError("Failed to parse item %r in %r" %
                           (href, self.path)) from e

    last_modified = time.strftime(
        "%a, %d %b %Y %H:%M:%S GMT",
        time.gmtime(time.time()))
    return EteSyncItem(self, item, href, last_modified=last_modified, etesync_item=etesync_item)
