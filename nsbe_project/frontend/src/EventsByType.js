import React, { useState, useEffect } from "react";
import axios from "axios";
import { useParams } from "react-router-dom";
import { Box, Grid, Link, Paper, Stack, Typography, Button } from "@mui/material";
import CalendarMonthTwoToneIcon from '@mui/icons-material/CalendarMonthTwoTone';
import RoomTwoTone from '@mui/icons-material/RoomTwoTone';
import { Link as RouterLink } from 'react-router-dom';
import Layout from './Layout';

function EventsByType() {
    const { eventType } = useParams();
    const [events, setEvents] = useState([]);

    useEffect(() => {
        async function fetchEvents() {
            try {
                const response = await axios.get(`http://127.0.0.1:8000/stage/events/${eventType}/`);
                setEvents(response.data);
            } catch(error) {
                console.log(error);
            }
        }
        fetchEvents();
    }, [eventType]);

    return (
        <Layout>
            <Box sx={{ padding: '20px' }}>
                <Box sx={{ textAlign: 'left', margin: '20px 0' }}>
                    <Typography variant="h3" sx={{ marginBottom: '20px' }}>
                        Events <span role="img" aria-label="calendar">📅</span>
                    </Typography>
                    <Box sx={{ display: 'flex', gap: '10px', marginBottom: '20px' }}>
                        <nav>
                            <Link
                                component={RouterLink} 
                                to="/events/upcoming" 
                                sx={{ textDecoration: 'none', fontSize: '16px', fontWeight: 'bold', marginRight: '10px' }}
                            >
                                Upcoming Events
                            </Link>
                            <Link
                                component={RouterLink} 
                                to="/events/past" 
                                sx={{ textDecoration: 'none', fontSize: '16px', fontWeight: 'bold' }}
                            >
                                Past Events
                            </Link>
                        </nav>
                    </Box>
                </Box>
                <Grid container spacing={2}>
                    {events.map(event => 
                        <Grid item xs={12} sm={6} md={4} key={event.id}>
                            <Paper elevation={3} sx={{ padding: '16px', textAlign: 'left' }}>
                                <Typography variant="h6">{event.title}</Typography>
                                <Stack spacing={1} sx={{ marginY: '10px' }}>
                                    <Stack alignItems="center" direction="row" gap={1}>
                                        <CalendarMonthTwoToneIcon />
                                        <Typography>{event.start_time} - {event.end_time}</Typography>           
                                    </Stack>
                                    <Stack alignItems="center" direction="row" gap={1}>
                                        <RoomTwoTone />
                                        <Typography>{event.location}</Typography>
                                    </Stack>
                                </Stack>
                                <Stack direction="row" spacing={2} sx={{ marginTop: '10px' }}>
                                    <Button
                                        variant="contained"
                                        sx={{ backgroundColor: '#F5F5F7', color: '#201414' }}
                                        href="#"
                                    >
                                        Register
                                    </Button>
                                    <Button
                                        variant="contained"
                                        sx={{ backgroundColor: '#2F2F96', color: '#F8EA31' }}
                                        href="#"
                                    >
                                        See Details
                                    </Button>
                                </Stack>
                            </Paper>
                        </Grid>
                    )}
                </Grid>
            </Box>
        </Layout>
    );
}

export default EventsByType;
