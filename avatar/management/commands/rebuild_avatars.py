from django.core.management.base import NoArgsCommand

from avatar.conf import settings
from avatar.models import Avatar


class Command(NoArgsCommand):
    help = ("Regenerates avatar thumbnails for the sizes specified in "
            "settings.AVATAR_AUTO_GENERATE_SIZES.")

    def handle_noargs(self, **options):
        sizes = getattr(settings, 'AUTO_GENERATE_AVATAR_SIZES', (80,))
        for avatar in sizes:
            for size in settings.AVATAR_AUTO_GENERATE_SIZES:
                print("Rebuilding Avatar id=%s at size %s." % (avatar.id, size))
                avatar.create_thumbnail(size)
