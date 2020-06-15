from rest_framework import serializers
from .models import Customer, Profession, Document, DataSheet


# Nested Relationships - to give user access to all serializers at once - single request
# this saves internet data
# NOTE: Nested Serializer have to be place before the main serializer that will be nesting,
# it's like objects within objects
class DataSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSheet
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    # assigning - def get_num_professions(self, obj) without get_
    # it gets it's value by calling a method on the serializer class
    # It can be used to ADD any sort of DATA to the serialized representation of your object.
    num_professions = serializers.SerializerMethodField(method_name=None)  # this is a read-only field
    # method_name - The name of the method on the serializer to be called.
    # If not included this defaults to get_<field_name>.

    # Nested Relationships - to give user access to DataSheetSerializer & CustomerSerializer at single request
    # this will display both the objects at once like object & nested object
    data_sheet = DataSheetSerializer()

    # to serialize the database relationship - foreignkey, one to one & many to many
    # StringRelatedField may be used to represent the target of the relationship using its __str__ method.
    # data_sheet = serializers.StringRelatedField()  # data_sheet - relationship filed in the modal
    # this will convert numeric data like pk of customer to string representation of object - description

    # same as above profession
    professions = serializers.StringRelatedField(many=True)  # many to many relationship

    # ForeignKey - one to many, document_set is the name of the ForeignKey relationship
    document_set = serializers.StringRelatedField(many=True)

    # NOTE: don't use (many=True) for one to one, it's for multiple relationships

    # PrimaryKeyRelatedField may be used to represent the target of the relationship using its primary key.
    # this will convert string representation of object to numeric data like pk, just the opposite of above

    class Meta:
        model = Customer
        fields = ('id', 'name', 'email', 'address', 'professions', 'data_sheet',
                  'active', 'status_message', 'num_professions', 'document_set')
        # added custom property method - status_message
        # added custom method from modal - num_professions

        # this method is define above without get_

    def get_num_professions(self, obj):
        return obj.num_professions()
        # calling handy method in the modal when it's not property,
        # including fields are not just enough in the serializers, so
        # to include logic, calculation, access data base - use this approach


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = '__all__'


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'
