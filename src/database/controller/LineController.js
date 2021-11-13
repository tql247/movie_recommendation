const LineService = require('../service/LineService');

class LineController {
    async createLine(req, res, next) {
        try {
            const lineData = req.body; // validate
            const lines = lineData.lines;
            const linesUploaded = [];

            await lines.forEach(async(line) => {
                line.line_idx = line.idx;
                line.source_id = lineData.source_id;
                line.coordinate = {
                    x1: line.x1,
                    x2: line.x2,
                    y1: line.y1,
                    y2: line.y2
                }

                linesUploaded.push(await LineService.createLine(line));
            })

            res.status(201).json(linesUploaded);
        } catch (err) {
            console.error(err);
            returnnext(err);
        }
    }
}

module.exports = new LineController();