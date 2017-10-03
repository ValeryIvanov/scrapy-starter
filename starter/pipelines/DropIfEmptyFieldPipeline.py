# -*- coding: utf-8 -*-

from scrapy.exceptions import DropItem

class DropIfEmptyFieldPipeline(object):

    def process_item(self, item, spider):
		return item
		'''
        if item['important_field']:
            return item
        else:
            raise DropItem("Missing important_field in %s" % item)
		'''
		