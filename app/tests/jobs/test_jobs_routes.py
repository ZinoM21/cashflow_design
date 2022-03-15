from app.jobs.routes import jobs

def test_choose_job_success(client):
    # Page loads
    response = client.get('/jobs')
    assert response.status_code == 200

def test_play_redirect(client):
    # Page redirects to /jobs
    response = client.get('/play')
    assert response.status_code == 302

def test_choose_job_success(client):
    # Every dynamic page loads
    for job in jobs:
        response = client.get(f'/jobs/{job}')
        assert response.status_code == 200