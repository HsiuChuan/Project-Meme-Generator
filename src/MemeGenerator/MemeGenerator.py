from PIL import Image, ImageDraw

class MemeGenerator():
    def __init__(self, output_dir):
        self.output_dir = output_dir

    def make_meme(self, img_path, text, author, width=500):
        """Create a Postcard With a Text Greeting

        Arguments:
            in_path {str} -- the file location for the input image.
            out_path {str} -- the desired location for the output image.
            crop {tuple} -- The crop rectangle, as a (left, upper, right, lower)-tuple. Default=None.
            width {int} -- The pixel width value. Default=None.
        Returns:
            str -- the file path to the output image.
        """
        img = Image.open(img_path)

        if width is not None:
            ratio = width/float(img.size[0])
            height = int(ratio*float(img.size[1]))
            img = img.resize((width, height), Image.NEAREST)

        if text is not None and author is not None:
            draw = ImageDraw.Draw(img)
            message = text + ' - ' + author
            draw.text((10, 400), message, fill='white')

        filename =  img_path.split('/')[-1]
        filename =  filename.split('.')[-2]+ '_resize.' + filename.split('.')[-1]
        output_path_with_filename = self.output_dir + filename
        
        img.save(output_path_with_filename)
        return output_path_with_filename
