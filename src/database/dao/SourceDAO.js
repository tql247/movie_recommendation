const db = require('../db/db');

class SourceDao {
    async createSource(company_id, station_id, source_path, thumbnail_uri, thumbnail_width, thumbnail_height, duration, created_by) {
        const [source] = await db('source').insert({
            company_id: company_id,
            station_id: station_id,
            source_path: source_path,
            thumbnail_uri: thumbnail_uri,
            thumbnail_width: thumbnail_width,
            thumbnail_height: thumbnail_height,
            duration: duration,
            created_by: created_by
        }).returning('*');

        return source;
    }

    async getSourcePath(created_by) {
        const source = await db('source').where({
            created_by: created_by,
        }).select('id', 'source_path')

        return source;
    }
}

module.exports = new SourceDao();