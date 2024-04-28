import Header from 'components/Header';
import { Suspense } from 'react';

const { Outlet } = require('react-router-dom');

const SharedLayout = () => {
  return (
    <div>
      <Header />

      <Suspense>
        <Outlet />
      </Suspense>
    </div>
  );
};

export default SharedLayout;
