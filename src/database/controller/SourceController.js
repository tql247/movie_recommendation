const SourceService = require('../service/SourceService');

class SourceController {
    async createSource(req, res) {
        try {

            const sourceReq = req.body;
            sourceReq.thumbnail_uri = req.fileUploadedURI;
            const source = await SourceService.createSource(sourceReq);

            res.status(201).json(source);
        } catch (err) {
            console.error(err);
            res.status(500).json("something went wrong");
        }
    }

    async getSourcePath(req, res) {
        try {

            const { created_by } = req.query;
            const source = await SourceService.getSourcePath(created_by) || [];

            res.status(201).json(source);
        } catch (err) {
            console.error(err);
            res.status(500).json("something went wrong");
        }
    }
}

module.exports = new SourceController();