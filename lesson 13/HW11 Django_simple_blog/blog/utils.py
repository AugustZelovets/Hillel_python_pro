from django.contrib.auth.mixins import AccessMixin
from django.template.defaultfilters import slugify
#from typing import Str


class StaffMixin(AccessMixin):
    """Verify that the current user is staff."""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


def generate_slug(self, classname, name_field) -> str:
    """
    slug generation from category name and <_number> if such slug already exists
    :param self: self.
    :param classname: Name of class in which you overwrite save() function
    :param name_field: field of current Model which displays the name or title of class object
    :return: generated slug
    """
    slugs = [object.slug for object in classname.objects.all()]
    index_ = 0
    new_slug = slugify(name_field)
    if new_slug in slugs:
        while new_slug + '_' + str(index_) in slugs:
            index_ += 1
        new_slug += '_' + str(index_)
    return new_slug
