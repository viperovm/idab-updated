from django.contrib import admin
from .models import Rating, History, Contact, Phone, Social, Review, Faq, Section, SubSection, AdmittanceDate
from adminsortable2.admin import SortableAdminMixin


class PhoneInline(admin.TabularInline):
    model = Phone


class SocialInline(admin.TabularInline):
    model = Social


class ContactAdmin(admin.ModelAdmin):
    inlines = [
        SocialInline,
        PhoneInline,
    ]


class AdmittanceDateAdmin(admin.ModelAdmin):
    model = AdmittanceDate


class HistoryAdmin(SortableAdminMixin, admin.ModelAdmin):
    model = History


class RatingAdmin(SortableAdminMixin, admin.ModelAdmin):
    model = Rating


admin.site.register(Phone)
admin.site.register(Social)
admin.site.register(Contact, ContactAdmin)
admin.site.register(AdmittanceDate, AdmittanceDateAdmin)
admin.site.register(History, HistoryAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Review)
admin.site.register(Faq)
admin.site.register(Section)
admin.site.register(SubSection)
