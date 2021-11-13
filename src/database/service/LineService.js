const LineDao = require('../dao/LineDao');

class LineService {
    createLine(sourceDTO) {
        const { source_id, coordinate, direction, line_idx } = sourceDTO;

        return LineDao.createLine(source_id, coordinate, direction, line_idx);
    }
}

module.exports = new LineService();