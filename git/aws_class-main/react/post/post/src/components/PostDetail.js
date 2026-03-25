import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';

const PostDetail = () => {
  const { id } = useParams();
  const [post, setPost] = useState(null);

  useEffect(() => {
    
    const getPostDetail = () => {
      
      const detailData = {
        id: id,
        title: `${id}번 게시글의 제목`,
        content: `${id}번 게시글의 상세 내용입니다.`,
        author: '바보'
      };
      setPost(detailData);
    };
    getPostDetail();
  }, [id]);

  if (!post) return <div>로딩 중...</div>;

  return (
    <div>
      
      <h1>게시글 상세</h1>
      <p><strong>번호:</strong> {post.id}</p>
      <p><strong>제목:</strong> {post.title}</p>
      <p><strong>내용:</strong> {post.content}</p>
      <p><strong>작성자:</strong> {post.author}</p>
    </div>
  );
};

export default PostDetail;