const db = require('../db/db');

class VideoDao {
    async createVideo(source_id, file_name) {
        const [video] = await db('video').insert({
            source_id: source_id,
            file_name: file_name,
        }).returning('*');

        return video;
    }
}

module.exports = new VideoDao();