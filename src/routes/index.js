// "use strict";
const express = require('express');
const router = express.Router();
const path = require('path');

router.get('/', (req, res) => {
    res.sendFile(path.join(process.cwd(), 'public/index.html'));
})

router.get('/test', (req, res) => {
    // io.emit('outside');
    res.send('hm');
})

const source = require('./source');
router.use('/source', source);

const line = require('./line');
router.use('/line', line);

const video = require('./video');
router.use('/video', video);

module.exports = router;