from django.contrib import admin

# Register your models here.

from .models import *

from import_export.admin import ImportExportModelAdmin

#AS IS
admin.site.register(Product, ImportExportModelAdmin)

#ANTHONY
admin.site.register(AnthonyStudent, ImportExportModelAdmin)
admin.site.register(AnthonyOffense)

#CHARLES
admin.site.register(CharlesStudent, ImportExportModelAdmin)
admin.site.register(CharlesOffense)

#BERCHMAN
admin.site.register(BerchmanStudent, ImportExportModelAdmin)
admin.site.register(BerchmanOffense)

#BOSCO
admin.site.register(BoscoStudent, ImportExportModelAdmin)
admin.site.register(BoscoOffense)

#JOSEPH
admin.site.register(JosephStudent, ImportExportModelAdmin)
admin.site.register(JosephOffense)

#MARTIN
admin.site.register(MartinStudent, ImportExportModelAdmin)
admin.site.register(MartinOffense)

#PAUL
admin.site.register(PaulStudent, ImportExportModelAdmin)
admin.site.register(PaulOffense)

#ANNE
admin.site.register(AnneStudent, ImportExportModelAdmin)
admin.site.register(AnneOffense)

#FAUSTINA
admin.site.register(FaustinaStudent, ImportExportModelAdmin)
admin.site.register(FaustinaOffense)

#MARY
admin.site.register(MaryStudent, ImportExportModelAdmin)
admin.site.register(MaryOffense)

#RITA
admin.site.register(RitaStudent, ImportExportModelAdmin)
admin.site.register(RitaOffense)

#ROSE
admin.site.register(RoseStudent, ImportExportModelAdmin)
admin.site.register(RoseOffense)

#TERESA
admin.site.register(TeresaStudent, ImportExportModelAdmin)
admin.site.register(TeresaOffense)
