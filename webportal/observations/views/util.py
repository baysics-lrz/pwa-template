import datetime
import os
from PIL import Image, ImageOps
from observations.models import Category1, Category2, Category3, Category4


def get_map_content():
    context = {"category1_list": Category1.objects.all(), "category2_list": Category2.objects.all(),
                "category3_list": Category3.objects.all(), "category4_list": Category4.objects.all()}
    return context


def create_thumbnail(fp):
        new_max_size = 400
        # check if it is a string path from the shell script
        if (type(fp) is str):
            im_photo = Image.open("media/" + fp)
        else: # otherwise treat it as image field
            im_photo = Image.open(fp)
        # transpose if the mobile phone rotation has a different orientation specified in exif
        try:
            # try if exif data is good
            print("trying PIL image transpose (exif_transpose)")
            im_photo = ImageOps.exif_transpose(im_photo)
        except:
            # bad exif - try transpose fix
            print("transpose failed")
            try:
                print("trying to fix transpose")
                exif = im_photo.getexif()
                orientation = exif.get(0x0112)
                transpose_method = {
                    2: Image.FLIP_LEFT_RIGHT,
                    3: Image.ROTATE_180,
                    4: Image.FLIP_TOP_BOTTOM,
                    5: Image.TRANSPOSE,
                    6: Image.ROTATE_270,
                    7: Image.TRANSVERSE,
                    8: Image.ROTATE_90
                }
                im_photo = im_photo.transpose(transpose_method[orientation])
            except:
                # couldn't fix, just ignore rotiation
                print("couldn't transpose")
                pass
        im_w = im_photo.size[0]
        im_h = im_photo.size[1]

        # check if image is larger than suggested size
        if im_w > new_max_size:
            im_factor = (im_w / new_max_size)
            im_w = int(im_w / im_factor)
            im_h = int(im_h / im_factor)

        # check if height is larger
        if im_h > new_max_size:
            im_factor = (im_h / new_max_size)
            im_h = int(im_h / im_factor)
            im_w = int(im_w / im_factor)

        # create a smaller image
        im_smaller = im_photo.resize((im_w, im_h))
        # changed path for resized photos/thumbnails
        new_fp = "media/thumbnails/" + str(fp)[:-4] + "_small.jpg"
        os.makedirs(os.path.dirname(new_fp), exist_ok=True)
        # check if image mode is different from RGB and convert
        if im_smaller.mode != "RGB":
            im_smaller = im_smaller.convert("RGB")
        print(im_smaller.mode)
        im_smaller.save(new_fp)
        print("saved", new_fp)

