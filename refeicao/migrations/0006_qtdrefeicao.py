# Generated by Django 4.1 on 2023-02-25 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('refeicao', '0005_alter_cardapio_almoco_alter_cardapio_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='QtdRefeicao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mes', models.CharField(choices=[('Janeiro', 'Janeiro'), ('Fevereiro', 'Fevereiro'), ('Março', 'Março'), ('Abril', 'Abril'), ('Maio', 'Maio'), ('Junho', 'Junho'), ('Julho', 'Julho'), ('Agosto', 'Agosto'), ('Setembro', 'Setembro'), ('Outubro', 'Outubro'), ('Novembro', 'Novembro'), ('Dezembro', 'Dezembro')], max_length=20)),
                ('ano', models.CharField(choices=[('2023', '2023'), ('2024', '2024'), ('2025', '2025'), ('2026', '2026'), ('2027', '2027'), ('2028', '2028'), ('2029', '2029'), ('2030', '2030'), ('2031', '2031'), ('2032', '2032'), ('2033', '2033'), ('2034', '2034'), ('2035', '2035'), ('2036', '2036'), ('2037', '2037'), ('2038', '2038'), ('2039', '2039'), ('2040', '2040'), ('2041', '2041'), ('2042', '2042'), ('2043', '2043'), ('2044', '2044'), ('2045', '2045'), ('2046', '2046'), ('2047', '2047'), ('2048', '2048'), ('2049', '2049'), ('2050', '2050'), ('2051', '2051'), ('2052', '2052'), ('2053', '2053'), ('2054', '2054'), ('2055', '2055'), ('2056', '2056'), ('2057', '2057'), ('2058', '2058'), ('2059', '2059'), ('2060', '2060'), ('2061', '2061'), ('2062', '2062'), ('2063', '2063'), ('2064', '2064'), ('2065', '2065'), ('2066', '2066'), ('2067', '2067'), ('2068', '2068'), ('2069', '2069'), ('2070', '2070'), ('2071', '2071'), ('2072', '2072'), ('2073', '2073'), ('2074', '2074'), ('2075', '2075'), ('2076', '2076'), ('2077', '2077'), ('2078', '2078'), ('2079', '2079'), ('2080', '2080'), ('2081', '2081'), ('2082', '2082'), ('2083', '2083'), ('2084', '2084'), ('2085', '2085'), ('2086', '2086'), ('2087', '2087'), ('2088', '2088'), ('2089', '2089'), ('2090', '2090'), ('2091', '2091'), ('2092', '2092'), ('2093', '2093'), ('2094', '2094'), ('2095', '2095'), ('2096', '2096'), ('2097', '2097'), ('2098', '2098'), ('2099', '2099')], max_length=4)),
                ('almocoQtd', models.IntegerField()),
                ('jantarQtd', models.IntegerField()),
            ],
        ),
    ]
