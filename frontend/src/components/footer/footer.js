import React from 'react'
import { Icon }  from '../index';
import './styles.scss'

export default () => {
  return (
    <footer>
      <div className='fix-bottom footer'>
        <span>
          <Icon link='https://github.com/Itsindigo/' target='_blank' title='ItsIndigo Github' img={process.env.PUBLIC_URL + '/github_logo.png'}  imageDimensions={['32px', '32px']}/>
          <Icon link='https://twitter.com/EatsIndigo' target='_blank' title='EatsIndigo Twitter' img={process.env.PUBLIC_URL + '/twitter_logo.png'} imageDimensions={['32px', '32px']} />
        </span>  
      </div>
    </footer>
  )
}
