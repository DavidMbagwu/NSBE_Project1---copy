import React from 'react';
import { Link as RouterLink } from 'react-router-dom';
import { Box, List, ListItem, ListItemText, Stack } from '@mui/material';
import { Home, Folder, Star, CalendarToday, Person, ExitToApp, Help, Info } from '@mui/icons-material';
import './Layout.css'; 
import nsbe5g from './static/stage/logo/nsbe5g.png';

const Layout = ({ children }) => {
  return (
    <Box className="wrapper">
      <Box className="sidebar">
        <Box className="sidebar-header">
          <img src={nsbe5g} alt="mcneese_icon" />
        </Box>
        <List className="list">
          <ListItem>
            <a href="http://127.0.0.1:8000/stage/" className="link">
              <Stack alignItems="center" direction="row" spacing={2}>
                <Home />
                <ListItemText primary="Home" />
              </Stack>
            </a>
          </ListItem>
          <ListItem>
            <a href="http://127.0.0.1:8000/stage/directory" className="link">
              <Stack alignItems="center" direction="row" spacing={2}>
                <Folder />
                <ListItemText primary="Directory" />
              </Stack>
            </a>
          </ListItem>
          <ListItem>
            <a href="http://127.0.0.1:8000/stage/points" className="link">
              <Stack alignItems="center" direction="row" spacing={2}>
                <Star />
                <ListItemText primary="Points" />
              </Stack>
            </a>
          </ListItem>
          <ListItem>
            <RouterLink to="/events" className="link">
              <Stack alignItems="center" direction="row" spacing={2}>
                <CalendarToday />
                <ListItemText primary="Events" />
              </Stack>
            </RouterLink>
          </ListItem>
          <ListItem>
            <a href="http://127.0.0.1:8000/stage/profile" className="link">
              <Stack alignItems="center" direction="row" spacing={2}>
                <Person />
                <ListItemText primary="Profile" />
              </Stack>
            </a>
          </ListItem>
        </List>
        <List className="bottom_list" sx={{ marginTop: '200px' }}>
          <ListItem>
            <a href="http://127.0.0.1:8000/stage/logout" className="link">
              <Stack alignItems="center" direction="row" spacing={2}>
                <ExitToApp />
                <ListItemText primary="Log Out" />
              </Stack>
            </a>
          </ListItem>
          <ListItem>
            <a href="http://127.0.0.1:8000/stage/help" className="link">
              <Stack alignItems="center" direction="row" spacing={2}>
                <Help />
                <ListItemText primary="Help" />
              </Stack>
            </a>
          </ListItem>
          <ListItem>
            <a href="http://127.0.0.1:8000/stage/about" className="link">
              <Stack alignItems="center" direction="row" spacing={2}>
                <Info />
                <ListItemText primary="About" />
              </Stack>
            </a>
          </ListItem>
        </List>
      </Box>
      <Box className="content">
        {children}
      </Box>
    </Box>
  );
};

export default Layout;
