const fs = require('fs');
const cloudinary = require("../../cloudinary.config");


async function cloudinaryUploader(req, res, next) {
    try {
        console.log('uploadedUri')
        console.log(req["file"])

        const uploadedUri = await cloudinary["uploader"].upload(
            req["file"].path, {
                resource_type: 'image'
            }
        );


        console.log('uploadedUri')
        console.log(uploadedUri["secure_url"])
        req.fileUploadedURI = uploadedUri["secure_url"];

        await fs.unlinkSync(req["file"].path);

        next();
    } catch (err) {
        console.error(err);
        return next(err);
    }
}

module.exports = cloudinaryUploader;