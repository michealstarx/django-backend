from .models import Smartify, News, Home, Books, Videos, Podcasts, Biology, Chemistry, English, Mathematics, Physics, BiNq, ChNq, CsNq, LaNq, MaNq, PhNq, AnatomyOne, AnatomyTwo, BiochemistryOne, BiochemistryTwo, ClinicalScienceOne, ClinicalScienceTwo, DiagnosticsOne, DiagnosticsTwo, LabScienceOne, LabScienceTwo, PathologyOne, PathologyTwo, PhysiologyOne, PhysiologyTwo, PublicHealthOne, PublicHealthTwo, SocietyAndMedicineOne, SocietyAndMedicineTwo, TherapeuticsOne, TherapeuticsTwo, AnatomyOnetbt, AnatomyTwotbt, BiochemistryOnetbt, BiochemistryTwotbt, ClinicalScienceOnetbt, ClinicalScienceTwotbt, DiagnosticsOnetbt, DiagnosticsTwotbt, LabScienceOnetbt, LabScienceTwotbt, PathologyOnetbt, PathologyTwotbt, PhysiologyOnetbt, PhysiologyTwotbt, PublicHealthOnetbt, PublicHealthTwotbt, SocietyAndMedicineOnetbt, SocietyAndMedicineTwotbt, TherapeuticsOnetbt, TherapeuticsTwotbt
from rest_framework import serializers


class SmartifySerializer(serializers.ModelSerializer):
    class Meta:
        model = Smartify
        fields = '__all__'

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

class HomeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = '__all__'

class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'

class VideosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Videos
        fields = '__all__'

class PodcastSerializers(serializers.ModelSerializer):
    class Meta:
        model = Podcasts
        fields = '__all__'

class BiologySerializers(serializers.ModelSerializer):
    class Meta:
        model = Biology
        fields = '__all__'

class ChemistrySerializers(serializers.ModelSerializer):
    class Meta:
        model = Chemistry
        fields = '__all__'

class EnglishSerializers(serializers.ModelSerializer):
    class Meta:
        model = English
        fields = '__all__'

class MathematicsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Mathematics
        fields = '__all__'

class PhysicsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Physics
        fields = '__all__'

class BiNqSerializers(serializers.ModelSerializer):
    class Meta:
        model = BiNq
        fields = '__all__'

class ChNqSerializers(serializers.ModelSerializer):
    class Meta:
        model = ChNq
        fields = '__all__'

class CsNqSerializers(serializers.ModelSerializer):
    class Meta:
        model = CsNq
        fields = '__all__'

class LaNqSerializers(serializers.ModelSerializer):
    class Meta:
        model = LaNq
        fields = '__all__'

class MaNqSerializers(serializers.ModelSerializer):
    class Meta:
        model = MaNq
        fields = '__all__'

class PhNqSerializers(serializers.ModelSerializer):
    class Meta:
        model = PhNq
        fields = '__all__'

class AnatomyOneSerializers(serializers.ModelSerializer):
    class Meta:
        model = AnatomyOne
        fields = '__all__'

class BiochemistryOneSerializers(serializers.ModelSerializer):
    class Meta:
        model = BiochemistryOne
        fields = '__all__'

class ClinicalScienceOneSerializers(serializers.ModelSerializer):
    class Meta:
        model = ClinicalScienceOne
        fields = '__all__'

class DiagnosticsOneSerializers(serializers.ModelSerializer):
    class Meta:
        model = DiagnosticsOne
        fields = '__all__'

class LabScienceOneSerializers(serializers.ModelSerializer):
    class Meta:
        model = LabScienceOne
        fields = '__all__'

class PathologyOneSerializers(serializers.ModelSerializer):
    class Meta:
        model = PathologyOne
        fields = '__all__'

class PhysiologyOneSerializers(serializers.ModelSerializer):
    class Meta:
        model = PhysiologyOne
        fields = '__all__'


class PublicHealthOneSerializers(serializers.ModelSerializer):
    class Meta:
        model = PublicHealthOne
        fields = '__all__'

class SocietyAndMedicineOneSerializers(serializers.ModelSerializer):
    class Meta:
        model = SocietyAndMedicineOne
        fields = '__all__'

class TherapeuticsOneSerializers(serializers.ModelSerializer):
    class Meta:
        model = TherapeuticsOne
        fields = '__all__'


class AnatomyTwoSerializers(serializers.ModelSerializer):
    class Meta:
        model = AnatomyTwo
        fields = '__all__'

class BiochemistryTwoSerializers(serializers.ModelSerializer):
    class Meta:
        model = BiochemistryTwo
        fields = '__all__'

class ClinicalScienceTwoSerializers(serializers.ModelSerializer):
    class Meta:
        model = ClinicalScienceTwo
        fields = '__all__'

class DiagnosticsTwoSerializers(serializers.ModelSerializer):
    class Meta:
        model = DiagnosticsTwo
        fields = '__all__'

class LabScienceTwoSerializers(serializers.ModelSerializer):
    class Meta:
        model = LabScienceTwo
        fields = '__all__'

class PathologyTwoSerializers(serializers.ModelSerializer):
    class Meta:
        model = PathologyTwo
        fields = '__all__'

class PhysiologyTwoSerializers(serializers.ModelSerializer):
    class Meta:
        model = PhysiologyTwo
        fields = '__all__'


class PublicHealthTwoSerializers(serializers.ModelSerializer):
    class Meta:
        model = PublicHealthTwo
        fields = '__all__'

class SocietyAndMedicineTwoSerializers(serializers.ModelSerializer):
    class Meta:
        model = SocietyAndMedicineTwo
        fields = '__all__'

class TherapeuticsTwoSerializers(serializers.ModelSerializer):
    class Meta:
        model = TherapeuticsTwo
        fields = '__all__'



class AnatomyOnetbtSerializers(serializers.ModelSerializer):
    class Meta:
        model = AnatomyOnetbt
        fields = '__all__'

class BiochemistryOnetbtSerializers(serializers.ModelSerializer):
    class Meta:
        model = BiochemistryOnetbt
        fields = '__all__'

class ClinicalScienceOnetbtSerializers(serializers.ModelSerializer):
    class Meta:
        model = ClinicalScienceOnetbt
        fields = '__all__'

class DiagnosticsOnetbtSerializers(serializers.ModelSerializer):
    class Meta:
        model = DiagnosticsOnetbt
        fields = '__all__'

class LabScienceOnetbtSerializers(serializers.ModelSerializer):
    class Meta:
        model = LabScienceOnetbt
        fields = '__all__'

class PathologyOnetbtSerializers(serializers.ModelSerializer):
    class Meta:
        model = PathologyOnetbt
        fields = '__all__'

class PhysiologyOnetbtSerializers(serializers.ModelSerializer):
    class Meta:
        model = PhysiologyOnetbt
        fields = '__all__'


class PublicHealthOnetbtSerializers(serializers.ModelSerializer):
    class Meta:
        model = PublicHealthOnetbt
        fields = '__all__'

class SocietyAndMedicineOnetbtSerializers(serializers.ModelSerializer):
    class Meta:
        model = SocietyAndMedicineOnetbt
        fields = '__all__'

class TherapeuticsOnetbtSerializers(serializers.ModelSerializer):
    class Meta:
        model = TherapeuticsOnetbt
        fields = '__all__'


class AnatomyTwotbtSerializers(serializers.ModelSerializer):
    class Meta:
        model = AnatomyTwotbt
        fields = '__all__'

class BiochemistryTwotbtSerializers(serializers.ModelSerializer):
    class Meta:
        model = BiochemistryTwotbt
        fields = '__all__'

class ClinicalScienceTwotbtSerializers(serializers.ModelSerializer):
    class Meta:
        model = ClinicalScienceTwotbt
        fields = '__all__'

class DiagnosticsTwotbtSerializers(serializers.ModelSerializer):
    class Meta:
        model = DiagnosticsTwotbt
        fields = '__all__'

class LabScienceTwotbtSerializers(serializers.ModelSerializer):
    class Meta:
        model = LabScienceTwotbt
        fields = '__all__'

class PathologyTwotbtSerializers(serializers.ModelSerializer):
    class Meta:
        model = PathologyTwotbt
        fields = '__all__'

class PhysiologyTwotbtSerializers(serializers.ModelSerializer):
    class Meta:
        model = PhysiologyTwotbt
        fields = '__all__'


class PublicHealthTwotbtSerializers(serializers.ModelSerializer):
    class Meta:
        model = PublicHealthTwotbt
        fields = '__all__'

class SocietyAndMedicineTwotbtSerializers(serializers.ModelSerializer):
    class Meta:
        model = SocietyAndMedicineTwotbt
        fields = '__all__'

class TherapeuticsTwotbtSerializers(serializers.ModelSerializer):
    class Meta:
        model = TherapeuticsTwotbt
        fields = '__all__'