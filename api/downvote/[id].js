const mongoose = require('mongoose');
mongoose.connect(process.env.MONGODB_URI, { useNewUrlParser: true, useUnifiedTopology: true });

const Comment = mongoose.model('Comment', new mongoose.Schema({
  content: String,
  upvotes: Number,
  downvotes: Number,
}));

module.exports = async (req, res) => {
  if (req.method === 'PUT') {
    const comment = await Comment.findById(req.query.id);
    comment.downvotes++;
    await comment.save();
    res.json(comment);
  }
};
