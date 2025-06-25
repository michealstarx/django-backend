
from django.db import models


class Smartify(models.Model):
    title = models.CharField(max_length=120, blank=True, null=True)
    date= models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    firstImage = models.CharField(max_length=120, blank=True, null=True)
    introFirst = models.TextField( blank=True, null=True)
    introSecond = models.TextField( blank=True, null=True)
    introThird = models.TextField( blank=True, null=True)
    introFourth = models.TextField( blank=True, null=True)
    secondImage= models.CharField(max_length=120, blank=True, null=True)
    fparaBoldOne = models.TextField( blank=True, null=True)
    firstParagraphOne = models.TextField( blank=True, null=True)
    firstParagraphTwo = models.TextField( blank=True, null=True)
    firstParagraphThree = models.TextField( blank=True, null=True)
    firstParagraphFour = models.TextField( blank=True, null=True)
    firstParagraphBoldTwo = models.TextField( blank=True, null=True)
    firstParagraphFive = models.TextField( blank=True, null=True)
    firstParagraphSix = models.TextField( blank=True, null=True)
    firstParagraphSeven = models.TextField( blank=True, null=True)
    firstParagraphEight = models.TextField( blank=True, null=True)
    firstParagraphBoldThree = models.TextField( blank=True, null=True)
    firstParagraphNine = models.TextField( blank=True, null=True)
    firstParagraphTen = models.TextField( blank=True, null=True)
    firstParagraphEleven = models.TextField( blank=True, null=True)
    firstParagraphTwelve = models.TextField( blank=True, null=True)
    firstParagraphBoldFour = models.TextField( blank=True, null=True)
    firstParagraphThirteen = models.TextField( blank=True, null=True)
    firstParagraphFourteen = models.TextField( blank=True, null=True)
    firstParagraphFifteen = models.TextField( blank=True, null=True)
    firstParagraphSixteen = models.TextField( blank=True, null=True)
    firstParagraphBoldFive = models.TextField( blank=True, null=True)
    firstParagraphSeventeen = models.TextField( blank=True, null=True)
    firstParagraphEighteen = models.TextField( blank=True, null=True)
    firstParagraphNineteen = models.TextField( blank=True, null=True)
    firstParagraphTwenty = models.TextField( blank=True, null=True)
    firstParagraphBoldSix = models.TextField( blank=True, null=True)
    firstParagraphTwentyone = models.TextField( blank=True, null=True)
    firstParagraphTwentytwo = models.TextField( blank=True, null=True)
    firstParagraphTwentythree = models.TextField( blank=True, null=True)
    firstParagraphTwentyfour = models.TextField( blank=True, null=True)
    firstParagraphBoldSeven = models.TextField( blank=True, null=True)
    firstParagraphTwentyfive = models.TextField( blank=True, null=True)
    firstParagraphTwentysix = models.TextField( blank=True, null=True)
    firstParagraphTwentyseven = models.TextField( blank=True, null=True)
    firstParagraphTwentyeight = models.TextField( blank=True, null=True)
    thirdImage = models.CharField(max_length=120, blank=True, null=True)
    secondParagraphBoldOne = models.TextField( blank=True, null=True)
    secondParagraphOne = models.TextField( blank=True, null=True)
    secondParagraphTwo = models.TextField( blank=True, null=True)
    secondParagraphThree = models.TextField( blank=True, null=True)
    secondParagraphFour = models.TextField( blank=True, null=True)
    secondParagraphBoldTwo = models.TextField( blank=True, null=True)
    secondParagraphFive = models.TextField( blank=True, null=True)
    secondParagraphSix = models.TextField( blank=True, null=True)
    secondParagraphSeven = models.TextField( blank=True, null=True)
    secondParagraphEight = models.TextField( blank=True, null=True)
    secondParagraphBoldThree = models.TextField( blank=True, null=True)
    secondParagraphNine = models.TextField( blank=True, null=True)
    secondParagraphTen = models.TextField( blank=True, null=True)
    secondParagraphEleven = models.TextField( blank=True, null=True)
    secondParagraphTwelve = models.TextField( blank=True, null=True)
    secondParagraphBoldFour = models.TextField( blank=True, null=True)
    secondParagraphThirteen = models.TextField( blank=True, null=True)
    secondParagraphFourteen = models.TextField( blank=True, null=True)
    secondParagraphFifteen = models.TextField( blank=True, null=True)
    secondParagraphSixteen = models.TextField( blank=True, null=True)
    secondParagraphBoldFive = models.TextField( blank=True, null=True)
    secondParagraphSeventeen = models.TextField( blank=True, null=True)
    secondParagraphEighteen = models.TextField( blank=True, null=True)
    secondParagraphNineteen = models.TextField( blank=True, null=True)
    secondParagraphTwenty = models.TextField( blank=True, null=True)
    secondParagraphBoldSix = models.TextField( blank=True, null=True)
    secondParagraphTwentyone = models.TextField( blank=True, null=True)
    secondParagraphTwentytwo = models.TextField( blank=True, null=True)
    secondParagraphTwentythree = models.TextField( blank=True, null=True)
    secondParagraphTwentyfour = models.TextField( blank=True, null=True)
    secondParagraphBoldSeven = models.TextField( blank=True, null=True)
    secondParagraphTwentyfive = models.TextField( blank=True, null=True)
    secondParagraphTwentysix = models.TextField( blank=True, null=True)
    secondParagraphTwentyseven = models.TextField( blank=True, null=True)
    secondParagraphTwentyeight = models.TextField( blank=True, null=True)
    oimg = models.CharField(max_length=120, blank=True, null=True)
    poster = models.TextField( blank=True, null=True)
    position = models.TextField( blank=True, null=True)



    def __str__(self):
        return self.title

class User(models.Model):
    full_name = models.CharField(max_length=70)
    phone_number = models.IntegerField()

    def __str__(self):
        return self.full_name

class News(models.Model):
    title = models.CharField(max_length=120, blank=True, null=True)
    date= models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    fimg = models.CharField(max_length=120, blank=True, null=True)
    introFirst = models.TextField( blank=True, null=True)
    fparaBOne = models.TextField( blank=True, null=True)
    fparaBTwo = models.TextField( blank=True, null=True)
    fparaBThree = models.TextField( blank=True, null=True)
    fparaBFour = models.TextField( blank=True, null=True)
    fparaBFive = models.TextField( blank=True, null=True)
    fparaBSix = models.TextField( blank=True, null=True)
    fparaBSeven = models.TextField( blank=True, null=True)


    simg= models.CharField(max_length=120, blank=True, null=True)
    introSecond = models.TextField( blank=True, null=True)
    fparaOne = models.TextField( blank=True, null=True)
    fparaTwo = models.TextField( blank=True, null=True)
    fparaThree = models.TextField( blank=True, null=True)
    fparaFour = models.TextField( blank=True, null=True)
    fparaFive = models.TextField( blank=True, null=True)
    fparaSix = models.TextField( blank=True, null=True)
    fparaSeven = models.TextField( blank=True, null=True)
    fparaEight = models.TextField( blank=True, null=True)
    fparaNine = models.TextField( blank=True, null=True)
    fparaTen = models.TextField( blank=True, null=True)
    fparaEleven = models.TextField( blank=True, null=True)
    fparaTwelve = models.TextField( blank=True, null=True)
    fparaThirteen = models.TextField( blank=True, null=True)
    fparaFourteen = models.TextField( blank=True, null=True)
    fparaFifteen = models.TextField( blank=True, null=True)
    fparaSixteen = models.TextField( blank=True, null=True)
    fparaSeventeen = models.TextField( blank=True, null=True)
    fparaEighteen = models.TextField( blank=True, null=True)

    timg = models.CharField(max_length=120, blank=True, null=True)
    introThird = models.TextField( blank=True, null=True)
    sparaOne = models.TextField( blank=True, null=True)
    sparaTwo = models.TextField( blank=True, null=True)
    sparaThree = models.TextField( blank=True, null=True)
    sparaFour = models.TextField( blank=True, null=True)
    sparaFive = models.TextField( blank=True, null=True)
    sparaSix = models.TextField( blank=True, null=True)
    sparaSeven = models.TextField( blank=True, null=True)
    sparaEight = models.TextField( blank=True, null=True)
    sparaNine = models.TextField( blank=True, null=True)
    sparaTen = models.TextField( blank=True, null=True)
    sparaEleven = models.TextField( blank=True, null=True)
    sparaTwelve = models.TextField( blank=True, null=True)
    sparaThirteen = models.TextField( blank=True, null=True)
    sparaFourteen = models.TextField( blank=True, null=True)
    sparaFifteen = models.TextField( blank=True, null=True)
    sparaSixteen = models.TextField( blank=True, null=True)
    sparaSeventeen = models.TextField( blank=True, null=True)
    sparaEighteen = models.TextField( blank=True, null=True)

    introFourth = models.TextField( blank=True, null=True)
    sparaBOne = models.TextField( blank=True, null=True)
    sparaBTwo = models.TextField( blank=True, null=True)
    sparaBThree = models.TextField( blank=True, null=True)
    sparaBFour = models.TextField( blank=True, null=True)
    sparaBFive = models.TextField( blank=True, null=True)
    sparaBSix = models.TextField( blank=True, null=True)
    sparaBSeven = models.TextField( blank=True, null=True)
    oimg = models.CharField(max_length=120, blank=True, null=True)
    outro = models.TextField( blank=True, null=True)



    def __str__(self):
        return self.title

class Home(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    quote = models.CharField(max_length=7000, blank=True, null=True)
    introduction = models.TextField(blank=True, null=True)

    # images
    imageOne = models.TextField(blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    linkOne = models.TextField(blank=True, null=True)
    numberOne = models.IntegerField(blank=True, null=True)

    imageTwo = models.TextField(blank=True, null=True)
    textTwo = models.TextField(blank=True, null=True)
    linkTwo = models.TextField(blank=True, null=True)
    numberTwo = models.IntegerField(blank=True, null=True)

    imageThree = models.TextField(blank=True, null=True)
    textThree = models.TextField(blank=True, null=True)
    linkThree = models.TextField(blank=True, null=True)
    numberThree = models.IntegerField(blank=True, null=True)

    imageFour = models.TextField(blank=True, null=True)
    textFour = models.TextField(blank=True, null=True)
    linkFour = models.TextField(blank=True, null=True)
    numberFour = models.IntegerField(blank=True, null=True)

    imageFive = models.TextField(blank=True, null=True)
    textFive = models.TextField(blank=True, null=True)
    linkFive = models.TextField(blank=True, null=True)
    numberFive = models.IntegerField(blank=True, null=True)

    imageSix = models.TextField(blank=True, null=True)
    textSix = models.TextField(blank=True, null=True)
    linkSix = models.TextField(blank=True, null=True)
    numberSix = models.IntegerField(blank=True, null=True)

    imageSeven = models.TextField(blank=True, null=True)
    textSeven = models.TextField(blank=True, null=True)
    linkSeven = models.TextField(blank=True, null=True)
    numberSeven = models.IntegerField(blank=True, null=True)

    imageEight = models.TextField(blank=True, null=True)
    textEight = models.TextField(blank=True, null=True)
    linkEight = models.TextField(blank=True, null=True)
    numberEight = models.IntegerField(blank=True, null=True)

    imageNine = models.TextField(blank=True, null=True)
    textNine = models.TextField(blank=True, null=True)
    linkNine = models.TextField(blank=True, null=True)
    numberNine = models.IntegerField(blank=True, null=True)

    imageTen = models.TextField(blank=True, null=True)
    textTen = models.TextField(blank=True, null=True)
    linkTen = models.TextField(blank=True, null=True)
    numberTen = models.IntegerField(blank=True, null=True)

    imageEleven = models.TextField(blank=True, null=True)
    textEleven = models.TextField(blank=True, null=True)
    linkEleven = models.TextField(blank=True, null=True)
    numberEleven = models.IntegerField(blank=True, null=True)

    imageTwelve = models.TextField(blank=True, null=True)
    textTwelve = models.TextField(blank=True, null=True)
    linkTwelve = models.TextField(blank=True, null=True)
    numberTwelve = models.IntegerField(blank=True, null=True)

    imageThirteen = models.TextField(blank=True, null=True)
    textThirteen = models.TextField(blank=True, null=True)
    linkThirteen = models.TextField(blank=True, null=True)
    numberThirteen = models.IntegerField(blank=True, null=True)

    imageFourteen = models.TextField(blank=True, null=True)
    textFourteen = models.TextField(blank=True, null=True)
    linkFourteen = models.TextField(blank=True, null=True)
    numberFourteen = models.IntegerField(blank=True, null=True)

    imageFifteen = models.TextField(blank=True, null=True)
    textFifteen = models.TextField(blank=True, null=True)
    linkFifteen = models.TextField(blank=True, null=True)
    numberFifteen = models.IntegerField(blank=True, null=True)

    imageSixteen = models.TextField(blank=True, null=True)
    textSixteen = models.TextField(blank=True, null=True)
    linkSixteen = models.TextField(blank=True, null=True)
    numberSixteen = models.IntegerField(blank=True, null=True)

    imageSeventeen = models.TextField(blank=True, null=True)
    textSeventeen = models.TextField(blank=True, null=True)
    linkSeventeen = models.TextField(blank=True, null=True)
    numberSeventeen = models.IntegerField(blank=True, null=True)

    imageEighteen = models.TextField(blank=True, null=True)
    textEighteen = models.TextField(blank=True, null=True)
    linkEighteen = models.TextField(blank=True, null=True)
    numberEighteen = models.IntegerField(blank=True, null=True)

    imageNineteen = models.TextField(blank=True, null=True)
    textNineteen = models.TextField(blank=True, null=True)
    linkNineteen = models.TextField(blank=True, null=True)
    numberNineteen = models.IntegerField(blank=True, null=True)

    imageTwenty = models.TextField(blank=True, null=True)
    textTwenty = models.TextField(blank=True, null=True)
    linkTwenty = models.TextField(blank=True, null=True)
    numberTwenty = models.IntegerField(blank=True, null=True)


    def __str__(self):
        return self.screen


class Books(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)


    title = models.CharField(max_length=1000, blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    free = models.CharField(max_length=120, blank=True, null=True)


    extraTwo = models.TextField(blank=True, null=True)
    extraThree = models.TextField(blank=True, null=True)



    def __str__(self):
        return self.title

class Podcasts(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)


    title = models.CharField(max_length=1000, blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    dimensionx = models.IntegerField(blank=True, null=True)
    dimensiony = models.IntegerField(blank=True, null=True)


    extraThree = models.TextField(blank=True, null=True)



    def __str__(self):
        return self.title

class Videos(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)

    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)


    title = models.CharField(max_length=1000, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    dimensionx = models.IntegerField(blank=True, null=True)
    dimensiony = models.IntegerField(blank=True, null=True)


    extraThree = models.TextField(blank=True, null=True)



    def __str__(self):
        return self.screen


class Biology(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    specificGrade = models.TextField(blank=True, null=True)

    title = models.CharField(max_length=1000, blank=True, null=True)

    price = models.IntegerField(blank=True, null=True)
    imageLink = models.TextField(blank=True, null=True)
    imagedimensionx = models.IntegerField(blank=True, null=True)
    imagedimensiony = models.IntegerField(blank=True, null=True)
    file = models.TextField(blank=True, null=True)
    fileLink = models.TextField(blank=True, null=True)
    brainBoosterText = models.TextField(blank=True, null=True)
    brainBoosterLink = models.TextField(blank=True, null=True)
    practiceTestText = models.TextField(blank=True, null=True)
    practiceTestLink = models.TextField(blank=True, null=True)
    practiceTestAnswerText = models.TextField(blank=True, null=True)
    practiceTestAnswerLink = models.TextField(blank=True, null=True)

    extraThree = models.TextField(blank=True, null=True)



    def __str__(self):
        return self.title

class Chemistry(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    specificGrade = models.TextField(blank=True, null=True)

    title = models.CharField(max_length=1000, blank=True, null=True)

    price = models.IntegerField(blank=True, null=True)
    imageLink = models.TextField(blank=True, null=True)
    imagedimensionx = models.IntegerField(blank=True, null=True)
    imagedimensiony = models.IntegerField(blank=True, null=True)
    file = models.TextField(blank=True, null=True)
    fileLink = models.TextField(blank=True, null=True)
    brainBoosterText = models.TextField(blank=True, null=True)
    brainBoosterLink = models.TextField(blank=True, null=True)
    practiceTestText = models.TextField(blank=True, null=True)
    practiceTestLink = models.TextField(blank=True, null=True)
    practiceTestAnswerText = models.TextField(blank=True, null=True)
    practiceTestAnswerLink = models.TextField(blank=True, null=True)

    extraThree = models.TextField(blank=True, null=True)



    def __str__(self):
        return self.title

class English(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    specificGrade = models.TextField(blank=True, null=True)

    title = models.CharField(max_length=1000, blank=True, null=True)

    price = models.IntegerField(blank=True, null=True)
    imageLink = models.TextField(blank=True, null=True)
    imagedimensionx = models.IntegerField(blank=True, null=True)
    imagedimensiony = models.IntegerField(blank=True, null=True)
    file = models.TextField(blank=True, null=True)
    fileLink = models.TextField(blank=True, null=True)
    brainBoosterText = models.TextField(blank=True, null=True)
    brainBoosterLink = models.TextField(blank=True, null=True)
    practiceTestText = models.TextField(blank=True, null=True)
    practiceTestLink = models.TextField(blank=True, null=True)
    practiceTestAnswerText = models.TextField(blank=True, null=True)
    practiceTestAnswerLink = models.TextField(blank=True, null=True)

    extraThree = models.TextField(blank=True, null=True)



    def __str__(self):
        return self.title

class Mathematics(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    specificGrade = models.TextField(blank=True, null=True)

    title = models.CharField(max_length=1000, blank=True, null=True)

    price = models.IntegerField(blank=True, null=True)
    imageLink = models.TextField(blank=True, null=True)
    imagedimensionx = models.IntegerField(blank=True, null=True)
    imagedimensiony = models.IntegerField(blank=True, null=True)
    file = models.TextField(blank=True, null=True)
    fileLink = models.TextField(blank=True, null=True)
    brainBoosterText = models.TextField(blank=True, null=True)
    brainBoosterLink = models.TextField(blank=True, null=True)
    practiceTestText = models.TextField(blank=True, null=True)
    practiceTestLink = models.TextField(blank=True, null=True)
    practiceTestAnswerText = models.TextField(blank=True, null=True)
    practiceTestAnswerLink = models.TextField(blank=True, null=True)

    extraThree = models.TextField(blank=True, null=True)



    def __str__(self):
        return self.title

class Physics(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    specificGrade = models.TextField(blank=True, null=True)

    title = models.CharField(max_length=1000, blank=True, null=True)

    price = models.IntegerField(blank=True, null=True)
    imageLink = models.TextField(blank=True, null=True)
    imagedimensionx = models.IntegerField(blank=True, null=True)
    imagedimensiony = models.IntegerField(blank=True, null=True)
    file = models.TextField(blank=True, null=True)
    fileLink = models.TextField(blank=True, null=True)
    brainBoosterText = models.TextField(blank=True, null=True)
    brainBoosterLink = models.TextField(blank=True, null=True)
    practiceTestText = models.TextField(blank=True, null=True)
    practiceTestLink = models.TextField(blank=True, null=True)
    practiceTestAnswerText = models.TextField(blank=True, null=True)
    practiceTestAnswerLink = models.TextField(blank=True, null=True)

    extraThree = models.TextField(blank=True, null=True)



    def __str__(self):
        return self.title


class BiNq(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)

    title = models.CharField(max_length=1000, blank=True, null=True)
    link = models.TextField(blank=True, null=True)


    extraThree = models.TextField(blank=True, null=True)



    def __str__(self):
        return self.title

class ChNq(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)

    title = models.CharField(max_length=1000, blank=True, null=True)
    link = models.TextField(blank=True, null=True)


    extraThree = models.TextField(blank=True, null=True)



    def __str__(self):
        return self.title

class CsNq(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)

    title = models.CharField(max_length=1000, blank=True, null=True)
    link = models.TextField(blank=True, null=True)


    extraThree = models.TextField(blank=True, null=True)



    def __str__(self):
        return self.title

class LaNq(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)

    title = models.CharField(max_length=1000, blank=True, null=True)
    link = models.TextField(blank=True, null=True)


    extraThree = models.TextField(blank=True, null=True)



    def __str__(self):
        return self.title

class MaNq(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)

    title = models.CharField(max_length=1000, blank=True, null=True)
    link = models.TextField(blank=True, null=True)


    extraThree = models.TextField(blank=True, null=True)



    def __str__(self):
        return self.title

class PhNq(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)

    title = models.CharField(max_length=1000, blank=True, null=True)
    link = models.TextField(blank=True, null=True)


    extraThree = models.TextField(blank=True, null=True)



    def __str__(self):
        return self.title

class AnatomyOne(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)

    title = models.CharField(max_length=1000, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)
    textTwo = models.TextField(blank=True, null=True)
    textTwoLink = models.TextField(blank=True, null=True)
    textThree = models.TextField(blank=True, null=True)
    textThreeLink = models.TextField(blank=True, null=True)
    textFour = models.TextField(blank=True, null=True)
    textFourLink = models.TextField(blank=True, null=True)
    textFive = models.TextField(blank=True, null=True)
    textFiveLink = models.TextField(blank=True, null=True)
    textSix = models.TextField(blank=True, null=True)
    textSixLink = models.TextField(blank=True, null=True)
    textSeven = models.TextField(blank=True, null=True)
    textSevenLink = models.TextField(blank=True, null=True)

    extraThree = models.TextField(blank=True, null=True)



    def __str__(self):
        return self.title

class AnatomyOnetbt(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)

    title = models.CharField(max_length=1000, blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)

    extraThree = models.TextField(blank=True, null=True)



    def __str__(self):
        return self.title

class BiochemistryOne(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)

    title = models.CharField(max_length=1000, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)
    textTwo = models.TextField(blank=True, null=True)
    textTwoLink = models.TextField(blank=True, null=True)
    textThree = models.TextField(blank=True, null=True)
    textThreeLink = models.TextField(blank=True, null=True)
    textFour = models.TextField(blank=True, null=True)
    textFourLink = models.TextField(blank=True, null=True)
    textFive = models.TextField(blank=True, null=True)
    textFiveLink = models.TextField(blank=True, null=True)
    textSix = models.TextField(blank=True, null=True)
    textSixLink = models.TextField(blank=True, null=True)
    textSeven = models.TextField(blank=True, null=True)
    textSevenLink = models.TextField(blank=True, null=True)


    extraThree = models.TextField(blank=True, null=True)



    def __str__(self):
        return self.title

class BiochemistryOnetbt(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)

    title = models.CharField(max_length=1000, blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)


    extraThree = models.TextField(blank=True, null=True)



    def __str__(self):
        return self.title

class ClinicalScienceOne(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)

    title = models.CharField(max_length=1000, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)
    textTwo = models.TextField(blank=True, null=True)
    textTwoLink = models.TextField(blank=True, null=True)
    textThree = models.TextField(blank=True, null=True)
    textThreeLink = models.TextField(blank=True, null=True)
    textFour = models.TextField(blank=True, null=True)
    textFourLink = models.TextField(blank=True, null=True)
    textFive = models.TextField(blank=True, null=True)
    textFiveLink = models.TextField(blank=True, null=True)
    textSix = models.TextField(blank=True, null=True)
    textSixLink = models.TextField(blank=True, null=True)
    textSeven = models.TextField(blank=True, null=True)
    textSevenLink = models.TextField(blank=True, null=True)


    extraThree = models.TextField(blank=True, null=True)



    def __str__(self):
        return self.title

class ClinicalScienceOnetbt(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)

    title = models.CharField(max_length=1000, blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)


    extraThree = models.TextField(blank=True, null=True)



    def __str__(self):
        return self.title


class DiagnosticsOne(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)

    title = models.CharField(max_length=1000, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)
    textTwo = models.TextField(blank=True, null=True)
    textTwoLink = models.TextField(blank=True, null=True)
    textThree = models.TextField(blank=True, null=True)
    textThreeLink = models.TextField(blank=True, null=True)
    textFour = models.TextField(blank=True, null=True)
    textFourLink = models.TextField(blank=True, null=True)
    textFive = models.TextField(blank=True, null=True)
    textFiveLink = models.TextField(blank=True, null=True)
    textSix = models.TextField(blank=True, null=True)
    textSixLink = models.TextField(blank=True, null=True)
    textSeven = models.TextField(blank=True, null=True)
    textSevenLink = models.TextField(blank=True, null=True)


    extraThree = models.TextField(blank=True, null=True)



    def __str__(self):
        return self.title

class DiagnosticsOnetbt(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)

    title = models.CharField(max_length=1000, blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)


    extraThree = models.TextField(blank=True, null=True)



    def __str__(self):
        return self.title

class LabScienceOne(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)

    title = models.CharField(max_length=1000, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)
    textTwo = models.TextField(blank=True, null=True)
    textTwoLink = models.TextField(blank=True, null=True)
    textThree = models.TextField(blank=True, null=True)
    textThreeLink = models.TextField(blank=True, null=True)
    textFour = models.TextField(blank=True, null=True)
    textFourLink = models.TextField(blank=True, null=True)
    textFive = models.TextField(blank=True, null=True)
    textFiveLink = models.TextField(blank=True, null=True)
    textSix = models.TextField(blank=True, null=True)
    textSixLink = models.TextField(blank=True, null=True)
    textSeven = models.TextField(blank=True, null=True)
    textSevenLink = models.TextField(blank=True, null=True)


    extraThree = models.TextField(blank=True, null=True)



    def __str__(self):
        return self.title

class LabScienceOnetbt(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)

    title = models.CharField(max_length=1000, blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)


    extraThree = models.TextField(blank=True, null=True)



    def __str__(self):
        return self.title

class PathologyOne(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)

    title = models.CharField(max_length=1000, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)
    textTwo = models.TextField(blank=True, null=True)
    textTwoLink = models.TextField(blank=True, null=True)
    textThree = models.TextField(blank=True, null=True)
    textThreeLink = models.TextField(blank=True, null=True)
    textFour = models.TextField(blank=True, null=True)
    textFourLink = models.TextField(blank=True, null=True)
    textFive = models.TextField(blank=True, null=True)
    textFiveLink = models.TextField(blank=True, null=True)
    textSix = models.TextField(blank=True, null=True)
    textSixLink = models.TextField(blank=True, null=True)
    textSeven = models.TextField(blank=True, null=True)
    textSevenLink = models.TextField(blank=True, null=True)


    extraThree = models.TextField(blank=True, null=True)



    def __str__(self):
        return self.title

class PathologyOnetbt(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)

    title = models.CharField(max_length=1000, blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)


    extraThree = models.TextField(blank=True, null=True)



    def __str__(self):
        return self.title

class PhysiologyOne(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)

    title = models.CharField(max_length=1000, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)
    textTwo = models.TextField(blank=True, null=True)
    textTwoLink = models.TextField(blank=True, null=True)
    textThree = models.TextField(blank=True, null=True)
    textThreeLink = models.TextField(blank=True, null=True)
    textFour = models.TextField(blank=True, null=True)
    textFourLink = models.TextField(blank=True, null=True)
    textFive = models.TextField(blank=True, null=True)
    textFiveLink = models.TextField(blank=True, null=True)
    textSix = models.TextField(blank=True, null=True)
    textSixLink = models.TextField(blank=True, null=True)
    textSeven = models.TextField(blank=True, null=True)
    textSevenLink = models.TextField(blank=True, null=True)


    extraThree = models.TextField(blank=True, null=True)



    def __str__(self):
        return self.title

class PhysiologyOnetbt(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)

    title = models.CharField(max_length=1000, blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)


    extraThree = models.TextField(blank=True, null=True)



    def __str__(self):
        return self.title

class PublicHealthOne(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)

    title = models.CharField(max_length=1000, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)
    textTwo = models.TextField(blank=True, null=True)
    textTwoLink = models.TextField(blank=True, null=True)
    textThree = models.TextField(blank=True, null=True)
    textThreeLink = models.TextField(blank=True, null=True)
    textFour = models.TextField(blank=True, null=True)
    textFourLink = models.TextField(blank=True, null=True)
    textFive = models.TextField(blank=True, null=True)
    textFiveLink = models.TextField(blank=True, null=True)
    textSix = models.TextField(blank=True, null=True)
    textSixLink = models.TextField(blank=True, null=True)
    textSeven = models.TextField(blank=True, null=True)
    textSevenLink = models.TextField(blank=True, null=True)


    extraThree = models.TextField(blank=True, null=True)



    def __str__(self):
        return self.title

class PublicHealthOnetbt(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)

    title = models.CharField(max_length=1000, blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)


    extraThree = models.TextField(blank=True, null=True)



    def __str__(self):
        return self.title

class SocietyAndMedicineOne(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)

    title = models.CharField(max_length=1000, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)
    textTwo = models.TextField(blank=True, null=True)
    textTwoLink = models.TextField(blank=True, null=True)
    textThree = models.TextField(blank=True, null=True)
    textThreeLink = models.TextField(blank=True, null=True)
    textFour = models.TextField(blank=True, null=True)
    textFourLink = models.TextField(blank=True, null=True)
    textFive = models.TextField(blank=True, null=True)
    textFiveLink = models.TextField(blank=True, null=True)
    textSix = models.TextField(blank=True, null=True)
    textSixLink = models.TextField(blank=True, null=True)
    textSeven = models.TextField(blank=True, null=True)
    textSevenLink = models.TextField(blank=True, null=True)


    extraThree = models.TextField(blank=True, null=True)



    def __str__(self):
        return self.title

class SocietyAndMedicineOnetbt(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)

    title = models.CharField(max_length=1000, blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)


    extraThree = models.TextField(blank=True, null=True)



    def __str__(self):
        return self.title

class TherapeuticsOne(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)

    title = models.CharField(max_length=1000, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)
    textTwo = models.TextField(blank=True, null=True)
    textTwoLink = models.TextField(blank=True, null=True)
    textThree = models.TextField(blank=True, null=True)
    textThreeLink = models.TextField(blank=True, null=True)
    textFour = models.TextField(blank=True, null=True)
    textFourLink = models.TextField(blank=True, null=True)
    textFive = models.TextField(blank=True, null=True)
    textFiveLink = models.TextField(blank=True, null=True)
    textSix = models.TextField(blank=True, null=True)
    textSixLink = models.TextField(blank=True, null=True)
    textSeven = models.TextField(blank=True, null=True)
    textSevenLink = models.TextField(blank=True, null=True)


    extraThree = models.TextField(blank=True, null=True)



    def __str__(self):
        return self.title

class TherapeuticsOnetbt(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)

    title = models.CharField(max_length=1000, blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)


    extraThree = models.TextField(blank=True, null=True)



    def __str__(self):
        return self.title

class AnatomyTwo(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)

    title = models.CharField(max_length=1000, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)
    textTwo = models.TextField(blank=True, null=True)
    textTwoLink = models.TextField(blank=True, null=True)
    textThree = models.TextField(blank=True, null=True)
    textThreeLink = models.TextField(blank=True, null=True)
    textFour = models.TextField(blank=True, null=True)
    textFourLink = models.TextField(blank=True, null=True)
    textFive = models.TextField(blank=True, null=True)
    textFiveLink = models.TextField(blank=True, null=True)
    textSix = models.TextField(blank=True, null=True)
    textSixLink = models.TextField(blank=True, null=True)
    textSeven = models.TextField(blank=True, null=True)
    textSevenLink = models.TextField(blank=True, null=True)

    extraThree = models.TextField(blank=True, null=True)



    def __str__(self):
        return self.title

class AnatomyTwotbt(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)

    title = models.CharField(max_length=1000, blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)

    extraThree = models.TextField(blank=True, null=True)



    def __str__(self):
        return self.title

class BiochemistryTwo(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)

    title = models.CharField(max_length=1000, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)
    textTwo = models.TextField(blank=True, null=True)
    textTwoLink = models.TextField(blank=True, null=True)
    textThree = models.TextField(blank=True, null=True)
    textThreeLink = models.TextField(blank=True, null=True)
    textFour = models.TextField(blank=True, null=True)
    textFourLink = models.TextField(blank=True, null=True)
    textFive = models.TextField(blank=True, null=True)
    textFiveLink = models.TextField(blank=True, null=True)
    textSix = models.TextField(blank=True, null=True)
    textSixLink = models.TextField(blank=True, null=True)
    textSeven = models.TextField(blank=True, null=True)
    textSevenLink = models.TextField(blank=True, null=True)


    extraThree = models.TextField(blank=True, null=True)



    def __str__(self):
        return self.title

class BiochemistryTwotbt(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)

    title = models.CharField(max_length=1000, blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)


    extraThree = models.TextField(blank=True, null=True)



    def __str__(self):
        return self.title

class ClinicalScienceTwo(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)

    title = models.CharField(max_length=1000, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)
    textTwo = models.TextField(blank=True, null=True)
    textTwoLink = models.TextField(blank=True, null=True)
    textThree = models.TextField(blank=True, null=True)
    textThreeLink = models.TextField(blank=True, null=True)
    textFour = models.TextField(blank=True, null=True)
    textFourLink = models.TextField(blank=True, null=True)
    textFive = models.TextField(blank=True, null=True)
    textFiveLink = models.TextField(blank=True, null=True)
    textSix = models.TextField(blank=True, null=True)
    textSixLink = models.TextField(blank=True, null=True)
    textSeven = models.TextField(blank=True, null=True)
    textSevenLink = models.TextField(blank=True, null=True)


    extraThree = models.TextField(blank=True, null=True)



    def __str__(self):
        return self.title

class ClinicalScienceTwotbt(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)

    title = models.CharField(max_length=1000, blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)


    extraThree = models.TextField(blank=True, null=True)



    def __str__(self):
        return self.title


class DiagnosticsTwo(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)

    title = models.CharField(max_length=1000, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)
    textTwo = models.TextField(blank=True, null=True)
    textTwoLink = models.TextField(blank=True, null=True)
    textThree = models.TextField(blank=True, null=True)
    textThreeLink = models.TextField(blank=True, null=True)
    textFour = models.TextField(blank=True, null=True)
    textFourLink = models.TextField(blank=True, null=True)
    textFive = models.TextField(blank=True, null=True)
    textFiveLink = models.TextField(blank=True, null=True)
    textSix = models.TextField(blank=True, null=True)
    textSixLink = models.TextField(blank=True, null=True)
    textSeven = models.TextField(blank=True, null=True)
    textSevenLink = models.TextField(blank=True, null=True)


    extraThree = models.TextField(blank=True, null=True)



    def __str__(self):
        return self.title

class DiagnosticsTwotbt(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)

    title = models.CharField(max_length=1000, blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)


    extraThree = models.TextField(blank=True, null=True)



    def __str__(self):
        return self.title

class LabScienceTwo(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)

    title = models.CharField(max_length=1000, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)
    textTwo = models.TextField(blank=True, null=True)
    textTwoLink = models.TextField(blank=True, null=True)
    textThree = models.TextField(blank=True, null=True)
    textThreeLink = models.TextField(blank=True, null=True)
    textFour = models.TextField(blank=True, null=True)
    textFourLink = models.TextField(blank=True, null=True)
    textFive = models.TextField(blank=True, null=True)
    textFiveLink = models.TextField(blank=True, null=True)
    textSix = models.TextField(blank=True, null=True)
    textSixLink = models.TextField(blank=True, null=True)
    textSeven = models.TextField(blank=True, null=True)
    textSevenLink = models.TextField(blank=True, null=True)


    extraThree = models.TextField(blank=True, null=True)



    def __str__(self):
        return self.title

class LabScienceTwotbt(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)

    title = models.CharField(max_length=1000, blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)


    extraThree = models.TextField(blank=True, null=True)



    def __str__(self):
        return self.title

class PathologyTwo(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)

    title = models.CharField(max_length=1000, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)
    textTwo = models.TextField(blank=True, null=True)
    textTwoLink = models.TextField(blank=True, null=True)
    textThree = models.TextField(blank=True, null=True)
    textThreeLink = models.TextField(blank=True, null=True)
    textFour = models.TextField(blank=True, null=True)
    textFourLink = models.TextField(blank=True, null=True)
    textFive = models.TextField(blank=True, null=True)
    textFiveLink = models.TextField(blank=True, null=True)
    textSix = models.TextField(blank=True, null=True)
    textSixLink = models.TextField(blank=True, null=True)
    textSeven = models.TextField(blank=True, null=True)
    textSevenLink = models.TextField(blank=True, null=True)


    extraThree = models.TextField(blank=True, null=True)



    def __str__(self):
        return self.title

class PathologyTwotbt(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)

    title = models.CharField(max_length=1000, blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)


    extraThree = models.TextField(blank=True, null=True)



    def __str__(self):
        return self.title

class PhysiologyTwo(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)

    title = models.CharField(max_length=1000, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)
    textTwo = models.TextField(blank=True, null=True)
    textTwoLink = models.TextField(blank=True, null=True)
    textThree = models.TextField(blank=True, null=True)
    textThreeLink = models.TextField(blank=True, null=True)
    textFour = models.TextField(blank=True, null=True)
    textFourLink = models.TextField(blank=True, null=True)
    textFive = models.TextField(blank=True, null=True)
    textFiveLink = models.TextField(blank=True, null=True)
    textSix = models.TextField(blank=True, null=True)
    textSixLink = models.TextField(blank=True, null=True)
    textSeven = models.TextField(blank=True, null=True)
    textSevenLink = models.TextField(blank=True, null=True)


    extraThree = models.TextField(blank=True, null=True)



    def __str__(self):
        return self.title

class PhysiologyTwotbt(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)

    title = models.CharField(max_length=1000, blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)


    extraThree = models.TextField(blank=True, null=True)



    def __str__(self):
        return self.title

class PublicHealthTwo(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)

    title = models.CharField(max_length=1000, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)
    textTwo = models.TextField(blank=True, null=True)
    textTwoLink = models.TextField(blank=True, null=True)
    textThree = models.TextField(blank=True, null=True)
    textThreeLink = models.TextField(blank=True, null=True)
    textFour = models.TextField(blank=True, null=True)
    textFourLink = models.TextField(blank=True, null=True)
    textFive = models.TextField(blank=True, null=True)
    textFiveLink = models.TextField(blank=True, null=True)
    textSix = models.TextField(blank=True, null=True)
    textSixLink = models.TextField(blank=True, null=True)
    textSeven = models.TextField(blank=True, null=True)
    textSevenLink = models.TextField(blank=True, null=True)


    extraThree = models.TextField(blank=True, null=True)



    def __str__(self):
        return self.title

class PublicHealthTwotbt(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)

    title = models.CharField(max_length=1000, blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)


    extraThree = models.TextField(blank=True, null=True)



    def __str__(self):
        return self.title

class SocietyAndMedicineTwo(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)

    title = models.CharField(max_length=1000, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)
    textTwo = models.TextField(blank=True, null=True)
    textTwoLink = models.TextField(blank=True, null=True)
    textThree = models.TextField(blank=True, null=True)
    textThreeLink = models.TextField(blank=True, null=True)
    textFour = models.TextField(blank=True, null=True)
    textFourLink = models.TextField(blank=True, null=True)
    textFive = models.TextField(blank=True, null=True)
    textFiveLink = models.TextField(blank=True, null=True)
    textSix = models.TextField(blank=True, null=True)
    textSixLink = models.TextField(blank=True, null=True)
    textSeven = models.TextField(blank=True, null=True)
    textSevenLink = models.TextField(blank=True, null=True)


    extraThree = models.TextField(blank=True, null=True)



    def __str__(self):
        return self.title

class SocietyAndMedicineTwotbt(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)

    title = models.CharField(max_length=1000, blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)


    extraThree = models.TextField(blank=True, null=True)



    def __str__(self):
        return self.title

class TherapeuticsTwo(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)

    title = models.CharField(max_length=1000, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)
    textTwo = models.TextField(blank=True, null=True)
    textTwoLink = models.TextField(blank=True, null=True)
    textThree = models.TextField(blank=True, null=True)
    textThreeLink = models.TextField(blank=True, null=True)
    textFour = models.TextField(blank=True, null=True)
    textFourLink = models.TextField(blank=True, null=True)
    textFive = models.TextField(blank=True, null=True)
    textFiveLink = models.TextField(blank=True, null=True)
    textSix = models.TextField(blank=True, null=True)
    textSixLink = models.TextField(blank=True, null=True)
    textSeven = models.TextField(blank=True, null=True)
    textSevenLink = models.TextField(blank=True, null=True)


    extraThree = models.TextField(blank=True, null=True)



    def __str__(self):
        return self.title

class TherapeuticsTwotbt(models.Model):
    screen = models.CharField(max_length=500, blank=True, null=True)
    extraOne = models.TextField(blank=True, null=True)
    extraTwo = models.TextField(blank=True, null=True)

    title = models.CharField(max_length=1000, blank=True, null=True)
    textOne = models.TextField(blank=True, null=True)
    textOneLink = models.TextField(blank=True, null=True)


    extraThree = models.TextField(blank=True, null=True)



    def __str__(self):
        return self.title

