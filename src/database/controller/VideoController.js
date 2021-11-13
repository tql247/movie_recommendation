const VideoService = require('../service/VideoService');

class VideoController {
    async createVideo(req, res) {
        try {
            // if (req.)
            const { source_id, file_name } = req.body;

            const video = await VideoService.createVideo({ source_id, file_name });

            res.status(201).json(video);
        } catch (err) {
            console.error(err);
            res.status(500).json("something went wrong");
        }
    }
}

module.exports = new VideoController();