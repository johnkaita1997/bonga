from rest_framework import serializers

from calls.models import Call


class CallsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Call
        fields = "__all__"

    def validate(self, data):
         callstamp = data['callstamp']
         exists = Call.objects.filter(callstamp = callstamp)
         if exists:
             data = {"details": "Call Log already exists"}
             raise serializers.ValidationError(detail=data)
         else:
            return data

