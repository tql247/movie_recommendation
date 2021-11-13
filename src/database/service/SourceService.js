const SourceDao = require('../dao/SourceDao');

class SourceService {
    createSource(sourceDTO) {
        const { company_id, station_id, source_path, thumbnail_uri, thumbnail_width, thumbnail_height, duration, created_by } = sourceDTO;

        return SourceDao.createSource(company_id, station_id, source_path, thumbnail_uri, thumbnail_width, thumbnail_height, duration, created_by);
    }

    getSourcePath(created_by) {
        return SourceDao.getSourcePath(created_by);
    }
}

module.exports = new SourceService();