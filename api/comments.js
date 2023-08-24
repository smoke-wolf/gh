const mongoose = require('mongoose');
mongoose.connect(process.env.MONGODB_URI, { useNewUrlParser: true, useUnifiedTopology: true });

const Comment = mongoose.model('Comment', new mongoose.Schema({
  content: String,
  upvotes: Number,
  downvotes: Number,
}));

module.exports = async (req, res) => {
  if (req.method === 'POST') {
    const { content } = req.body;
    const newComment = new Comment({ content, upvotes: 0, downvotes: 0 });
    await newComment.save();
    res.status(201).json(newComment);
  } else if (req.method === 'GET') {
    const comments = await Comment.find().sort({ upvotes: -1 });
    res.json(comments);
  }
};
