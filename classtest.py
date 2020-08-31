from datetime import datetime


class Testing(object):
    def method(self):
        return "This method is called from server now: {}".format(
            datetime.now().strftime("%d-%m-%Y - (%H:%M:%S)")
        )
