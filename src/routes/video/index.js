const express = require('express');
const VideoController = require('../../database/controller/VideoController');
const router = express.Router();

router.post('/create', VideoController.createVideo)

module.exports = router;