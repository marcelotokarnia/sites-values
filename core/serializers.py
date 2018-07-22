from core.models import Site
from rest_framework import serializers


class SitesSerializer(serializers.HyperlinkedModelSerializer):
    def to_representation(self, obj):
        detailed = self.context['request'].GET.get('detailed')
        dicj = obj.to_dict_json()
        if detailed is not None:
            dicj['values'] = [val.to_dict_json() for val in obj.values.all()]
        return dicj

    class Meta:
        model = Site
        fields = ('name', 'values')
