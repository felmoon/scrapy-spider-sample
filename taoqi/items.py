from scrapy.item import Item, Field



class TaoqiItem(Item):
    # define the fields for your item here like:
        name = Field()
        description = Field()
        url = Field()
