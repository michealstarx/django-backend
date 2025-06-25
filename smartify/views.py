from django.shortcuts import render, redirect

from .form import UseR

from .models import Smartify, News, Home, Books, Videos, Podcasts, Biology, Chemistry, English, Mathematics, Physics, BiNq, ChNq, CsNq, LaNq, MaNq, PhNq, AnatomyOne, AnatomyTwo, BiochemistryOne, BiochemistryTwo, ClinicalScienceOne, ClinicalScienceTwo, DiagnosticsOne, DiagnosticsTwo, LabScienceOne, LabScienceTwo, PathologyOne, PathologyTwo, PhysiologyOne, PhysiologyTwo, PublicHealthOne, PublicHealthTwo, SocietyAndMedicineOne, SocietyAndMedicineTwo, TherapeuticsOne, TherapeuticsTwo, AnatomyOnetbt, AnatomyTwotbt, BiochemistryOnetbt, BiochemistryTwotbt, ClinicalScienceOnetbt, ClinicalScienceTwotbt, DiagnosticsOnetbt, DiagnosticsTwotbt, LabScienceOnetbt, LabScienceTwotbt, PathologyOnetbt, PathologyTwotbt, PhysiologyOnetbt, PhysiologyTwotbt, PublicHealthOnetbt, PublicHealthTwotbt, SocietyAndMedicineOnetbt, SocietyAndMedicineTwotbt, TherapeuticsOnetbt, TherapeuticsTwotbt
from .serializers import SmartifySerializer, NewsSerializer, HomeSerializers, BookSerializers, VideosSerializers, PodcastSerializers, BiologySerializers, ChemistrySerializers, EnglishSerializers, MathematicsSerializers, PhysicsSerializers, BiNqSerializers, ChNqSerializers, CsNqSerializers, LaNqSerializers, MaNqSerializers, PhNqSerializers, AnatomyOneSerializers, AnatomyTwoSerializers, BiochemistryOneSerializers, BiochemistryTwoSerializers, ClinicalScienceOneSerializers, ClinicalScienceTwoSerializers, DiagnosticsOneSerializers, DiagnosticsTwoSerializers, LabScienceOneSerializers, LabScienceTwoSerializers, PathologyOneSerializers, PathologyTwoSerializers, PhysiologyOneSerializers, PhysiologyTwoSerializers, PublicHealthOneSerializers, PublicHealthTwoSerializers, SocietyAndMedicineOneSerializers, SocietyAndMedicineTwoSerializers, TherapeuticsOneSerializers, TherapeuticsTwoSerializers, AnatomyOnetbtSerializers, AnatomyTwotbtSerializers, BiochemistryOnetbtSerializers, BiochemistryTwotbtSerializers, ClinicalScienceOnetbtSerializers, ClinicalScienceTwotbtSerializers, DiagnosticsOnetbtSerializers, DiagnosticsTwotbtSerializers, LabScienceOnetbtSerializers, LabScienceTwotbtSerializers, PathologyOnetbtSerializers, PathologyTwotbtSerializers, PhysiologyOnetbtSerializers, PhysiologyTwotbtSerializers, PublicHealthOnetbtSerializers, PublicHealthTwotbtSerializers, SocietyAndMedicineOnetbtSerializers, SocietyAndMedicineTwotbtSerializers, TherapeuticsOnetbtSerializers, TherapeuticsTwotbtSerializers
from rest_framework import mixins, generics, viewsets


def register(request):
    studystar = 'https://www.studystar.me'
    user = UseR(request.POST or None)
    if user.is_valid():
        user.save()
        return redirect(studystar)

    else:
        user = UseR()
    context = {
        'UseR': user
    }

    return render(request, 'smartify/register.html', context)



class List(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = SmartifySerializer
    queryset = Smartify.objects.all()

class Data(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = SmartifySerializer
    queryset = Smartify.objects.all()

    lookup_field = 'id'

class NewsList(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = NewsSerializer
    queryset = News.objects.all()

class NewsData(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = NewsSerializer
    queryset = News.objects.all()

    lookup_field = 'id'

class HomeList(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = HomeSerializers
    queryset = Home.objects.all()

class HomeDetails (viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = HomeSerializers
    queryset = Home.objects.all()

    lookup_field = 'id'

class BookList(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = BookSerializers
    queryset = Books.objects.all()

class BookDetails (viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = BookSerializers
    queryset = Books.objects.all()

    lookup_field = 'id'

class VideosList(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = VideosSerializers
    queryset = Videos.objects.all()

class VideosDetails (viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = VideosSerializers
    queryset = Videos.objects.all()

    lookup_field = 'id'

class PodcastsList(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = PodcastSerializers
    queryset = Podcasts.objects.all()

class PodcastsDetails (viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = PodcastSerializers
    queryset = Podcasts.objects.all()

    lookup_field = 'id'

class BiologyList(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = BiologySerializers
    queryset = Biology.objects.all()

class BiologyDetails (viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = BiologySerializers
    queryset = Biology.objects.all()

    lookup_field = 'id'

class ChemistryList(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = ChemistrySerializers
    queryset = Chemistry.objects.all()

class ChemistryDetails (viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = ChemistrySerializers
    queryset = Chemistry.objects.all()

    lookup_field = 'id'

class EnglishList(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = EnglishSerializers
    queryset = English.objects.all()

class EnglishDetails (viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = EnglishSerializers
    queryset = English.objects.all()

    lookup_field = 'id'

class MathematicsList(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = MathematicsSerializers
    queryset = Mathematics.objects.all()

class MathematicsDetails (viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = MathematicsSerializers
    queryset = Mathematics.objects.all()

    lookup_field = 'id'

class PhysicsList(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = PhysicsSerializers
    queryset = Physics.objects.all()

class PhysicsDetails (viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = PhysicsSerializers
    queryset = Physics.objects.all()

    lookup_field = 'id'

class BiNqList(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = BiNqSerializers
    queryset = BiNq.objects.all()

class BiNqDetails (viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = BiNqSerializers
    queryset = BiNq.objects.all()

    lookup_field = 'id'

class ChNqList(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = ChNqSerializers
    queryset = ChNq.objects.all()

class ChNqDetails (viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = ChNqSerializers
    queryset = ChNq.objects.all()

    lookup_field = 'id'

class CsNqList(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = CsNqSerializers
    queryset = CsNq.objects.all()

class CsNqDetails (viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = CsNqSerializers
    queryset = CsNq.objects.all()

    lookup_field = 'id'

class LaNqList(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = LaNqSerializers
    queryset = LaNq.objects.all()

class LaNqDetails (viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = LaNqSerializers
    queryset = LaNq.objects.all()

    lookup_field = 'id'

class MaNqList(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = MaNqSerializers
    queryset = MaNq.objects.all()

class MaNqDetails (viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = MaNqSerializers
    queryset = MaNq.objects.all()

    lookup_field = 'id'

class PhNqList(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = PhNqSerializers
    queryset = PhNq.objects.all()

class PhNqDetails (viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = PhNqSerializers
    queryset = PhNq.objects.all()

    lookup_field = 'id'

class AnatomyOneList(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = AnatomyOneSerializers
    queryset = AnatomyOne.objects.all()

class AnatomyOneDetails (viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = AnatomyOneSerializers
    queryset = AnatomyOne.objects.all()

    lookup_field = 'id'

class BiochemistryOneList(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = BiochemistryOneSerializers
    queryset = BiochemistryOne.objects.all()

class BiochemistryOneDetails (viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = BiochemistryOneSerializers
    queryset = BiochemistryOne.objects.all()

    lookup_field = 'id'

class ClinicalScienceOneList(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = ClinicalScienceOneSerializers
    queryset = ClinicalScienceOne.objects.all()

class ClinicalScienceOneDetails (viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = ClinicalScienceOneSerializers
    queryset = ClinicalScienceOne.objects.all()

    lookup_field = 'id'

class DiagnosticsOneList(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = DiagnosticsOneSerializers
    queryset = DiagnosticsOne.objects.all()

class DiagnosticsOneDetails (viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = DiagnosticsOneSerializers
    queryset = DiagnosticsOne.objects.all()

    lookup_field = 'id'

class LabScienceOneList(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = LabScienceOneSerializers
    queryset = LabScienceOne.objects.all()

class LabScienceOneDetails (viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = LabScienceOneSerializers
    queryset = LabScienceOne.objects.all()

    lookup_field = 'id'

class PathologyOneList(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = PathologyOneSerializers
    queryset = PathologyOne.objects.all()

class PathologyOneDetails (viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = PathologyOneSerializers
    queryset = PathologyOne.objects.all()

    lookup_field = 'id'

class PhysiologyOneList(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = PhysiologyOneSerializers
    queryset = PhysiologyOne.objects.all()

class PhysiologyOneDetails (viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = PhysiologyOneSerializers
    queryset = PhysiologyOne.objects.all()

    lookup_field = 'id'

class PublicHealthOneList(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = PublicHealthOneSerializers
    queryset = PublicHealthOne.objects.all()

class PublicHealthOneDetails (viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = PublicHealthOneSerializers
    queryset = PublicHealthOne.objects.all()

    lookup_field = 'id'

class SocietyAndMedicineOneList(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = SocietyAndMedicineOneSerializers
    queryset = SocietyAndMedicineOne.objects.all()

class SocietyAndMedicineOneDetails (viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = SocietyAndMedicineOneSerializers
    queryset = SocietyAndMedicineOne.objects.all()

    lookup_field = 'id'

class TherapeuticsOneList(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = TherapeuticsOneSerializers
    queryset = TherapeuticsOne.objects.all()

class TherapeuticsOneDetails (viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = TherapeuticsOneSerializers
    queryset = TherapeuticsOne.objects.all()

    lookup_field = 'id'

class AnatomyTwoList(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = AnatomyTwoSerializers
    queryset = AnatomyTwo.objects.all()

class AnatomyTwoDetails (viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = AnatomyTwoSerializers
    queryset = AnatomyTwo.objects.all()

    lookup_field = 'id'

class BiochemistryTwoList(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = BiochemistryTwoSerializers
    queryset = BiochemistryTwo.objects.all()

class BiochemistryTwoDetails (viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = BiochemistryTwoSerializers
    queryset = BiochemistryTwo.objects.all()

    lookup_field = 'id'

class ClinicalScienceTwoList(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = ClinicalScienceTwoSerializers
    queryset = ClinicalScienceTwo.objects.all()

class ClinicalScienceTwoDetails (viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = ClinicalScienceTwoSerializers
    queryset = ClinicalScienceTwo.objects.all()

    lookup_field = 'id'

class DiagnosticsTwoList(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = DiagnosticsTwoSerializers
    queryset = DiagnosticsTwo.objects.all()

class DiagnosticsTwoDetails (viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = DiagnosticsTwoSerializers
    queryset = DiagnosticsTwo.objects.all()

    lookup_field = 'id'

class LabScienceTwoList(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = LabScienceTwoSerializers
    queryset = LabScienceTwo.objects.all()

class LabScienceTwoDetails (viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = LabScienceTwoSerializers
    queryset = LabScienceTwo.objects.all()

    lookup_field = 'id'

class PathologyTwoList(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = PathologyTwoSerializers
    queryset = PathologyTwo.objects.all()

class PathologyTwoDetails (viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = PathologyTwoSerializers
    queryset = PathologyTwo.objects.all()

    lookup_field = 'id'

class PhysiologyTwoList(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = PhysiologyTwoSerializers
    queryset = PhysiologyTwo.objects.all()

class PhysiologyTwoDetails (viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = PhysiologyTwoSerializers
    queryset = PhysiologyTwo.objects.all()

    lookup_field = 'id'

class PublicHealthTwoList(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = PublicHealthTwoSerializers
    queryset = PublicHealthTwo.objects.all()

class PublicHealthTwoDetails (viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = PublicHealthTwoSerializers
    queryset = PublicHealthTwo.objects.all()

    lookup_field = 'id'

class SocietyAndMedicineTwoList(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = SocietyAndMedicineTwoSerializers
    queryset = SocietyAndMedicineTwo.objects.all()

class SocietyAndMedicineTwoDetails (viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = SocietyAndMedicineTwoSerializers
    queryset = SocietyAndMedicineTwo.objects.all()

    lookup_field = 'id'

class TherapeuticsTwoList(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = TherapeuticsTwoSerializers
    queryset = TherapeuticsTwo.objects.all()

class TherapeuticsTwoDetails (viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = TherapeuticsTwoSerializers
    queryset = TherapeuticsTwo.objects.all()

    lookup_field = 'id'




class AnatomyOnetbtList(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = AnatomyOnetbtSerializers
    queryset = AnatomyOnetbt.objects.all()

class AnatomyOnetbtDetails (viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = AnatomyOnetbtSerializers
    queryset = AnatomyOnetbt.objects.all()

    lookup_field = 'id'

class BiochemistryOnetbtList(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = BiochemistryOnetbtSerializers
    queryset = BiochemistryOnetbt.objects.all()

class BiochemistryOnetbtDetails (viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = BiochemistryOnetbtSerializers
    queryset = BiochemistryOnetbt.objects.all()

    lookup_field = 'id'

class ClinicalScienceOnetbtList(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = ClinicalScienceOnetbtSerializers
    queryset = ClinicalScienceOnetbt.objects.all()

class ClinicalScienceOnetbtDetails (viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = ClinicalScienceOnetbtSerializers
    queryset = ClinicalScienceOnetbt.objects.all()

    lookup_field = 'id'

class DiagnosticsOnetbtList(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = DiagnosticsOnetbtSerializers
    queryset = DiagnosticsOnetbt.objects.all()

class DiagnosticsOnetbtDetails (viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = DiagnosticsOnetbtSerializers
    queryset = DiagnosticsOnetbt.objects.all()

    lookup_field = 'id'

class LabScienceOnetbtList(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = LabScienceOnetbtSerializers
    queryset = LabScienceOnetbt.objects.all()

class LabScienceOnetbtDetails (viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = LabScienceOnetbtSerializers
    queryset = LabScienceOnetbt.objects.all()

    lookup_field = 'id'

class PathologyOnetbtList(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = PathologyOnetbtSerializers
    queryset = PathologyOnetbt.objects.all()

class PathologyOnetbtDetails (viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = PathologyOnetbtSerializers
    queryset = PathologyOnetbt.objects.all()

    lookup_field = 'id'

class PhysiologyOnetbtList(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = PhysiologyOnetbtSerializers
    queryset = PhysiologyOnetbt.objects.all()

class PhysiologyOnetbtDetails (viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = PhysiologyOnetbtSerializers
    queryset = PhysiologyOnetbt.objects.all()

    lookup_field = 'id'

class PublicHealthOnetbtList(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = PublicHealthOnetbtSerializers
    queryset = PublicHealthOnetbt.objects.all()

class PublicHealthOnetbtDetails (viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = PublicHealthOnetbtSerializers
    queryset = PublicHealthOnetbt.objects.all()

    lookup_field = 'id'

class SocietyAndMedicineOnetbtList(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = SocietyAndMedicineOnetbtSerializers
    queryset = SocietyAndMedicineOnetbt.objects.all()

class SocietyAndMedicineOnetbtDetails (viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = SocietyAndMedicineOnetbtSerializers
    queryset = SocietyAndMedicineOnetbt.objects.all()

    lookup_field = 'id'

class TherapeuticsOnetbtList(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = TherapeuticsOnetbtSerializers
    queryset = TherapeuticsOnetbt.objects.all()

class TherapeuticsOnetbtDetails (viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = TherapeuticsOnetbtSerializers
    queryset = TherapeuticsOnetbt.objects.all()

    lookup_field = 'id'

class AnatomyTwotbtList(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = AnatomyTwotbtSerializers
    queryset = AnatomyTwotbt.objects.all()

class AnatomyTwotbtDetails (viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = AnatomyTwotbtSerializers
    queryset = AnatomyTwotbt.objects.all()

    lookup_field = 'id'

class BiochemistryTwotbtList(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = BiochemistryTwotbtSerializers
    queryset = BiochemistryTwotbt.objects.all()

class BiochemistryTwotbtDetails (viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = BiochemistryTwotbtSerializers
    queryset = BiochemistryTwotbt.objects.all()

    lookup_field = 'id'

class ClinicalScienceTwotbtList(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = ClinicalScienceTwotbtSerializers
    queryset = ClinicalScienceTwotbt.objects.all()

class ClinicalScienceTwotbtDetails (viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = ClinicalScienceTwotbtSerializers
    queryset = ClinicalScienceTwotbt.objects.all()

    lookup_field = 'id'

class DiagnosticsTwotbtList(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = DiagnosticsTwotbtSerializers
    queryset = DiagnosticsTwotbt.objects.all()

class DiagnosticsTwotbtDetails (viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = DiagnosticsTwotbtSerializers
    queryset = DiagnosticsTwotbt.objects.all()

    lookup_field = 'id'

class LabScienceTwotbtList(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = LabScienceTwotbtSerializers
    queryset = LabScienceTwotbt.objects.all()

class LabScienceTwotbtDetails (viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = LabScienceTwotbtSerializers
    queryset = LabScienceTwotbt.objects.all()

    lookup_field = 'id'

class PathologyTwotbtList(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = PathologyTwotbtSerializers
    queryset = PathologyTwotbt.objects.all()

class PathologyTwotbtDetails (viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = PathologyTwotbtSerializers
    queryset = PathologyTwotbt.objects.all()

    lookup_field = 'id'

class PhysiologyTwotbtList(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = PhysiologyTwotbtSerializers
    queryset = PhysiologyTwotbt.objects.all()

class PhysiologyTwotbtDetails (viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = PhysiologyTwotbtSerializers
    queryset = PhysiologyTwotbt.objects.all()

    lookup_field = 'id'

class PublicHealthTwotbtList(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = PublicHealthTwotbtSerializers
    queryset = PublicHealthTwotbt.objects.all()

class PublicHealthTwotbtDetails (viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = PublicHealthTwotbtSerializers
    queryset = PublicHealthTwotbt.objects.all()

    lookup_field = 'id'

class SocietyAndMedicineTwotbtList(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = SocietyAndMedicineTwotbtSerializers
    queryset = SocietyAndMedicineTwotbt.objects.all()

class SocietyAndMedicineTwotbtDetails (viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = SocietyAndMedicineTwotbtSerializers
    queryset = SocietyAndMedicineTwotbt.objects.all()

    lookup_field = 'id'

class TherapeuticsTwotbtList(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = TherapeuticsTwotbtSerializers
    queryset = TherapeuticsTwotbt.objects.all()

class TherapeuticsTwotbtDetails (viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = TherapeuticsTwotbtSerializers
    queryset = TherapeuticsTwotbt.objects.all()

    lookup_field = 'id'