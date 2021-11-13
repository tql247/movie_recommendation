const express = require('express');
const SourceController = require('../../database/controller/SourceController');
const router = express.Router();
const uploader = require("../../middlewares/uploader");
const cloudinaryUploader = require("../../middlewares/cloudinaryUploader");

// using uploader middlewares with input name thumbnail
router.post('/create', [uploader.single('thumbnail'), cloudinaryUploader], SourceController.createSource)

router.get('/source_path', SourceController.getSourcePath)

module.exports = router;