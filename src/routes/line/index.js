const express = require('express');
const LineController = require('../../database/controller/LineController');
const router = express.Router();

router.post('/create', LineController.createLine)

module.exports = router;