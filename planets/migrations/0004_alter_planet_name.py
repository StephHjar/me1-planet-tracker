# Generated by Django 3.2.16 on 2022-11-26 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planets', '0003_alter_planet_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planet',
            name='name',
            field=models.CharField(choices=[['---------', '---------'], ['Agebinium', 'Agebinium'], ['Ageko', 'Ageko'], ['Agetoton', 'Agetoton'], ['Alko', 'Alko'], ['Almarcrux', 'Almarcrux'], ['Almos', 'Almos'], ['Alrumter', 'Alrumter'], ['Alsages', 'Alsages'], ['Altaaya', 'Altaaya'], ['Altahe', 'Altahe'], ['Altanorch', 'Altanorch'], ['Amaranthine', 'Amaranthine'], ['Antibaar', 'Antibaar'], ['Antida', 'Antida'], ['Antiroprus', 'Antiroprus'], ['Antirumgon', 'Antirumgon'], ['Antitarra', 'Antitarra'], ['Apo', 'Apo'], ['Arcadia', 'Arcadia'], ['Archanes', 'Archanes'], ['Armeni', 'Armeni'], ['Asteroid X57', 'Asteroid X57'], ['Benda', 'Benda'], ['Binthu', 'Binthu'], ['Borr', 'Borr'], ['Camaron', 'Camaron'], ['Canctra', 'Canctra'], ['Canrum', 'Canrum'], ['Casbin', 'Casbin'], ['Chasca', 'Chasca'], ['Chofen', 'Chofen'], ['Chohe', 'Chohe'], ['Circe', 'Circe'], ['Citadel', 'Citadel'], ['Clobaka', 'Clobaka'], ['Clocrolis', 'Clocrolis'], ['Clojiia', 'Clojiia'], ['Clomarthu', 'Clomarthu'], ['Cloroplon', 'Cloroplon'], ['Clotanca', 'Clotanca'], ['Clugon', 'Clugon'], ['Derneuca', 'Derneuca'], ['Dregir', 'Dregir'], ['Earth', 'Earth'], ['Eden Prime', 'Eden Prime'], ['Edmos', 'Edmos'], ['Edolus', 'Edolus'], ['Eletania', 'Eletania'], ['Farcrothu', 'Farcrothu'], ['Fargeluse', 'Fargeluse'], ['Faringor', 'Faringor'], ['Farnuri', 'Farnuri'], ['Farthorl', 'Farthorl'], ['Feros', 'Feros'], ['Gremar', 'Gremar'], ['Gromar', 'Gromar'], ['Grosalgen', 'Grosalgen'], ['Hunidor', 'Hunidor'], ['Huningto', 'Huningto'], ['Hunsalra', 'Hunsalra'], ['Illapa', 'Illapa'], ['Ilos', 'Ilos'], ['Imaneya', 'Imaneya'], ["Intai'sei", "Intai'sei"], ['Inti', 'Inti'], ['Jarfor', 'Jarfor'], ['Jartar', 'Jartar'], ['Juncro', 'Juncro'], ['Juntauma', 'Juntauma'], ['Junthor', 'Junthor'], ['Jupiter', 'Jupiter'], ['Klencory', 'Klencory'], ['Klendagon', 'Klendagon'], ['Klensal', 'Klensal'], ['Logan', 'Logan'], ['Loki', 'Loki'], ['Luna', 'Luna'], ['Maganlis', 'Maganlis'], ['Maidla', 'Maidla'], ['Maji', 'Maji'], ['Mars', 'Mars'], ['Matar', 'Matar'], ['Matol', 'Matol'], ['Mavigon', 'Mavigon'], ['Mawinor', 'Mawinor'], ['Mercury', 'Mercury'], ['Metgos', 'Metgos'], ['Mingito', 'Mingito'], ['Morana', 'Morana'], ['MSV Cornucopia', 'MSV Cornucopia'], ['MSV Fedele', 'MSV Fedele'], ['MSV Majesty', 'MSV Majesty'], ['MSV Ontario', 'MSV Ontario'], ['MSV Worthington', 'MSV Worthington'], ['Nausicaa', 'Nausicaa'], ['Nearrum', 'Nearrum'], ['Nemata', 'Nemata'], ['Nepheron', 'Nepheron'], ['Nepmos', 'Nepmos'], ['Nepneu', 'Nepneu'], ['Neptune', 'Neptune'], ['Nirvana', 'Nirvana'], ['Nodacrux', 'Nodacrux'], ['Nonuel', 'Nonuel'], ['Notanban', 'Notanban'], ['Noveria', 'Noveria'], ['Ontaheter', 'Ontaheter'], ['Ontamalca', 'Ontamalca'], ['Ontarom', 'Ontarom'], ['Parag', 'Parag'], ['Paravin', 'Paravin'], ['Pataiton', 'Pataiton'], ['Patajiri', 'Patajiri'], ['Patamalrus', 'Patamalrus'], ['Patashi', 'Patashi'], ['Patatanlis', 'Patatanlis'], ['Patavig', 'Patavig'], ['Phaistos', 'Phaistos'], ['Pharos', 'Pharos'], ['Ploba', 'Ploba'], ['Pluto', 'Pluto'], ['Pomal', 'Pomal'], ['Porolan', 'Porolan'], ['Pregel', 'Pregel'], ['Prescyla', 'Prescyla'], ['Presrop', 'Presrop'], ['Pressha', 'Pressha'], ['Proteus', 'Proteus'], ['Quaji', 'Quaji'], ['Quana', 'Quana'], ['Rayingri', 'Rayingri'], ['Raysha', 'Raysha'], ['Renshato', 'Renshato'], ['Salamis', 'Salamis'], ['Saturn', 'Saturn'], ['Sesmose', 'Sesmose'], ['Sharblu', 'Sharblu'], ['Sharjila', 'Sharjila'], ['Sharring', 'Sharring'], ['Slekon', 'Slekon'], ['Sogelrus', 'Sogelrus'], ['Solcrum', 'Solcrum'], ['Solmarlon', 'Solmarlon'], ['Sonedma', 'Sonedma'], ['Supay', 'Supay'], ['Svarog', 'Svarog'], ['Syba', 'Syba'], ['Sybin', 'Sybin'], ['Syided', 'Syided'], ['Sylsalto', 'Sylsalto'], ['Sytau', 'Sytau'], ['Tamahera', 'Tamahera'], ['Terra Nova', 'Terra Nova'], ['Tharopto', 'Tharopto'], ['Thegeuse', 'Thegeuse'], ['Therum', 'Therum'], ['Therumlon', 'Therumlon'], ['Thesalgon', 'Thesalgon'], ['Theshaca', 'Theshaca'], ['Theyar', 'Theyar'], ['Treagir', 'Treagir'], ['Trebin', 'Trebin'], ['Trelyn', 'Trelyn'], ['Tremanre', 'Tremanre'], ['Tremar', 'Tremar'], ['Treyarmus', 'Treyarmus'], ['Tungel', 'Tungel'], ['Tunshagon', 'Tunshagon'], ['Tuntau', 'Tuntau'], ['Tyr', 'Tyr'], ['Unidentified Space Facility', 'Unidentified Space Facility'], ['Uranus', 'Uranus'], ['Varmalus', 'Varmalus'], ['Vebinok', 'Vebinok'], ['Vectra', 'Vectra'], ['Veles', 'Veles'], ['Vemal', 'Vemal'], ['Venus', 'Venus'], ['Veyaria', 'Veyaria'], ['Virmire', 'Virmire'], ['Wentania', 'Wentania'], ['Wermani', 'Wermani'], ['Wuo', 'Wuo'], ['Xamarri', 'Xamarri'], ['Xanadu', 'Xanadu'], ['Xathorron', 'Xathorron'], ['Xawin', 'Xawin'], ['Yunthorl', 'Yunthorl'], ['Zafe', 'Zafe'], ['Zaherux', 'Zaherux'], ['Zakros', 'Zakros'], ['Zatorus', 'Zatorus'], ['Zayarter', 'Zayarter'], ['Zion', 'Zion']], max_length=200, null=True),
        ),
    ]