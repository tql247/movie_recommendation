const VideoDao = require('../dao/VideoDao');

class VideoService {
    createVideo(videoDTO) {
        const { source_id, file_name } = videoDTO;

        return VideoDao.createVideo(source_id, file_name);
    }
}

module.exports = new VideoService();