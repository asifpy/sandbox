from crudbuilder.abstract import BaseCrudBuilder

from .models import Band


class BandCrud(BaseCrudBuilder):
    model = Band
    search_feilds = ['name']
    tables2_fields = ('name', 'can_rock')
    tables2_css_class = "table table-bordered table-condensed"
    tables2_pagination = 10  # default is 10
    modelform_excludes = ['created_by', 'updated_by']
