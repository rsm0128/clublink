# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-08-07 19:10
from __future__ import unicode_literals

from django.db import migrations


EVERYONE_VISIBILITY = 0
MEMBERS_ONLY_VISIBILITY = 1
NON_MEMBERS_ONLY_VISIBILITY = 2


ALIASES = {
    'linkline/guest-fees': {
        'alias': 'membership/guest-fees',
        'name_en': 'Guest Fees',
        'visibility': MEMBERS_ONLY_VISIBILITY,
        'sort': 1,
    },
    'my-club/gallery': {
        'alias': 'about/gallery',
        'name_en': 'Gallery',
        'visibility': MEMBERS_ONLY_VISIBILITY,
        'sort': 2,
    },
    'my-club/team': {
        'alias': 'about/team',
        'name_en': 'Our Team',
        'visibility': MEMBERS_ONLY_VISIBILITY,
        'sort': 3,
    },
    'my-club/golf-shop': {
        'alias': 'about/golf-shop',
        'name_en': 'Golf Shop',
        'visibility': MEMBERS_ONLY_VISIBILITY,
        'sort': 4,
    },
}


def create_aliases(apps, schema_editor):
    Club = apps.get_model('clubs', 'Club')
    ClubPage = apps.get_model('cms', 'ClubPage')

    for club in Club.objects.all():
        if club.slug:
            for full_path in ALIASES:
                parent_path = full_path.split('/')
                slug = parent_path.pop()
                parent_path = '/'.join(parent_path)

                parent = None
                if parent_path:
                    try:
                        parent = ClubPage.objects.get(full_path=parent_path, club=club)
                    except ClubPage.DoesNotExist:
                        continue

                page, _ = ClubPage.objects.get_or_create(
                    full_path=full_path, slug=slug, parent=parent, club=club,
                    defaults={'is_locked': True})

                props = {**ALIASES[full_path]}

                if 'alias' in props:
                    try:
                        props['alias'] = ClubPage.objects.get(
                            full_path=props['alias'], club=club)
                    except ClubPage.DoesNotExist:
                        continue

                for prop in props:
                    setattr(page, prop, props[prop])

                page.save()


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0060_clubpage_alias'),
    ]

    operations = [
        migrations.RunPython(create_aliases, lambda x, y: None),
    ]
