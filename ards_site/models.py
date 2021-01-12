from django.db import models

'''
"_id": ObjectId(),
"name": "",
"role": "Captain",
"type": "Bowler/Batsman/All-rounder",
“team”: “firstXi / secondXi / u13 / u15”
"dateJoined": "dd/mm/yyyy",
"awards": [
    {
        "id": ObjectId(),
        "year": year,
        "type": " Bowling/Batting ",
    },
],
"mobile": "",
"bowling" : [
                {
                        "id" : ObjectId(),
                        "date" : new Date("2020-05-20"),
                        "overs" : 5,
                        "runs" : 20,
                        "wickets" : [ “bowled”, “caught”],
                        "extras" : 3
                }
        ],
"batting" : [
                {
                        "id" : ObjectId(),
                        "date" : new Date("2020-05-20"),
                        "4s" : 3,
                        "6s" : 1,
                        "runs" : 32,
                        "out" : "bowled"
                }
        ],

'''


class Team(models.Model):
    name = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=20, default='')

    def __str__(self):
        return str(self.name)


class Member(models.Model):
    name = models.CharField(max_length=40, default='')
    dateOfBirth = models.DateField(blank=True, null=True)
    role = models.ManyToManyField(Role)
    type = models.ManyToManyField(Type)
    teamsPlayedFor = models.ManyToManyField(Team)
    dateJoined = models.DateField(blank=True, null=True)
    mobile = models.CharField(max_length=15, default='')

    def __str__(self):
        return str(self.name)


class Cup(models.Model):
    name = models.CharField(max_length=30, default='')

    def __str__(self):
        return str(self.name)


class Awards(models.Model):
    type = models.ForeignKey(Cup, on_delete=models.CASCADE)
    year = models.IntegerField(blank=True, null=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return str('{0} {1} {2},'.format(self.member, self.type, self.year))


class Wicket(models.Model):
    name = models.CharField(max_length=20, default='')

    def __str__(self):
        return str(self.name)


class Opponent(models.Model):
    name = models.CharField(max_length=30, default='')

    def __str__(self):
        return str(self.name)


class Batting(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    opponent = models.ManyToManyField(Opponent)
    date = models.DateField(blank=True, null=True)
    fours = models.IntegerField(blank=True, null=True)
    sixes = models.IntegerField(blank=True, null=True)
    runs = models.IntegerField(blank=True, null=True)
    out = models.ManyToManyField(Wicket)

    def __str__(self):
        return str('Member={0}, Date={1}'.format(self.member, self.date))


class Bowling(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    opponent = models.ManyToManyField(Opponent)
    date = models.DateField(blank=True, null=True)
    overs = models.IntegerField(blank=True, null=True)
    runs = models.IntegerField(blank=True, null=True)
    wickets = models.IntegerField(blank=True, null=True)
    extras = models.CharField(max_length=20, default='')

    def __str__(self):
        return str('Member={0}, Date={1}'.format(self.member, self.date))
