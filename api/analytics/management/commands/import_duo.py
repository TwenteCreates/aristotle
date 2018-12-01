import requests
from django.core.management.base import BaseCommand, CommandError
from analytics.models import *

class Command(BaseCommand):
    help = 'imports duo data to the PrimarySchool model'

    def handle(self, *args, **options):
        try:
            request = requests.get('https://api.duo.nl/v0/datasets/01-hoofdvestigingen-bo')
        except requests.exceptions.RequestException as e:
            raise CommandError('Error getting API data')
        else:
            for r in request.json()['results']:
                PrimarySchool.objects.create(
                        straatnaam_correspondentie_adres=r["STRAATNAAM CORRESPONDENTIEADRES"],
                        nodaal_gebied_naam=r["NODAAL GEBIED NAAM"],
                        gemeentenaam=r["GEMEENTENAAM"],
                        rmc_regio_naam=r["RMC-REGIO NAAM"],
                        rpa_gebied_naam=r["RPA-GEBIED NAAM"],
                        wgr_gebied_code=r["WGR-GEBIED CODE"],
                        postcode=r["POSTCODE"],
                        postcode_correspondentie_adres=r["POSTCODE CORRESPONDENTIEADRES"],
                        gemeente_nummer=r["GEMEENTENUMMER"],
                        onderwijsgebied_naam=r["ONDERWIJSGEBIED NAAM"],
                        plaatsnaam=r["PLAATSNAAM"],
                        plaatsnaam_correspondentieadres=r["PLAATSNAAM CORRESPONDENTIEADRES"],
                        denominatie=r["DENOMINATIE"],
                        coropgebied_naam=r["COROPGEBIED NAAM"],
                        brin_nummer=r["BRIN NUMMER"],
                        nodaal_gebied_code=r["NODAAL GEBIED CODE"],
                        bevoegd_gezag_nummer=r["BEVOEGD GEZAG NUMMER"],
                        internetadres=r["INTERNETADRES"],
                        provincie=r["PROVINCIE"],
                        wgr_gebied_naam=r["WGR-GEBIED NAAM"],
                        rmc_regio_code=r["RMC-REGIO CODE"],
                        huisnummer_toevoeging=r["HUISNUMMER-TOEVOEGING"],
                        rpa_gebied_code=r["RPA-GEBIED CODE"],
                        instellings_naam=r["INSTELLINGSNAAM"],
                        huisnummer_toevoeging_correspondentieadres=r["HUISNUMMER-TOEVOEGING CORRESPONDENTIEADRES"],
                        onderwijsgebied_code=r["ONDERWIJSGEBIED CODE"],
                        coropgebied_code=r["COROPGEBIED CODE"],
                        straatnaam=r["STRAATNAAM"],
                        telefoonnummer=r["TELEFOONNUMMER"],
                        )
