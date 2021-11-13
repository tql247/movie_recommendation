const db = require('../db/db');

class LineDao {
    async createLine(source_id, coordinate, direction, line_idx) {
        const [line] = await db('line').insert({
            source_id,
            coordinate,
            direction,
            line_idx
        }).returning('*');

        return line;
    }
}

module.exports = new LineDao();