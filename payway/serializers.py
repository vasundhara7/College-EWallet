from rest_framework import serializers
from payway.models import paywaylog
from payway.mypay import payfunc

class PaywayLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = paywaylog
        fields = ('id', 'flag', 'cardid', 'amount')
        read_only_fields = ('flag',)

    def create(self, validated_data):
        cardid = validated_data['cardid']
        amount = validated_data['amount']
        flag = payfunc()
        paylog = paywaylog.objects.create(flag = flag, cardid = cardid, amount = amount)
        return paylog
