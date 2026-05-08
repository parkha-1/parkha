import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';

const Posts = () => {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    
    const getPosts = () => {
      const data = [
        { id: 1, title: '1번 게시물' },
        { id: 2, title: '2번 게시물' },
        { id: 3, title: '3번 게시물' }
      ];
      setPosts(data);
    };
    getPosts();
  }, []);

  return (
    <div>
      <h1>게시글 목록</h1>
      
      <ul>
        {posts.map((post) => (
          <li key={post.id}>
            
            <Link to={`/post/detail/${post.id}`}>{post.title}</Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Posts;